from django.contrib import messages
from django.db import connection
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from SuperPizzas.utils import verify_position
from users.forms import SignUpForm
from users.views import signup
from .forms import *
from .models import *
import sys

from django.core.management import call_command




def plan_management(request, plan_id=None):
    if plan_id:
        plan = get_object_or_404(Plan, id=plan_id)
    else:
        plan = None
    Module.initial_modules()
    form = PlanForm(instance=plan)

    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan guardado correctamente")
            form = PlanForm()
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(
        request,
        "franchises/plan_management.html",
        {"form": form, "plans": Plan.objects.all()},
    )


#@verify_position(allowed_positions=[User.FRANCHISE])
def register_franchise(request, plan_id=1):
    plan = Plan.search(plan_id)
    if not plan:
        messages.error(request, "No existe el plan buscado")
        return redirect("home")

    if request.method == "POST":
        form_franchise = FranchiseForm(request.POST)
        form_user = SignUpForm(request.POST)
        if form_franchise.is_valid() and form_user.is_valid():

            from django.db import connection
            try:
                user, user_response = signup(request,user_type='admin')
                franchise = form_franchise.save(commit=False)
                franchise.client = user
                franchise.plan = plan
                franchise.save()
                domain = Domain(
                    domain=f"{franchise.schema_name}.{settings.DOMAIN}",
                    is_primary=True,
                    tenant=franchise,
                )
                domain.save()
                connection.set_tenant(franchise)
                User.initial_user(email=franchise.client.email, hash_password=franchise.client.password)
                connection.set_schema_to_public()
                messages.success(request, "La franquicia ha sido creada exitosamente")
                return redirect("franchise_list")
            except:
                messages.error(
                    request, "No se pudo registrar la franquicia, contacte al soporte"
                )
        else:
            messages.error(
                request, "No se pudo registrar la franquicia, contacte al soporte"
            )
    else:
        form_franchise = FranchiseForm()
        form_user = SignUpForm()

    return render(
        request,
        "franchises/registry_franchises.html",
        {
            "form_franchise": form_franchise,
            "form_user":form_user,
            "title": "Franchise registry",
            "domains": Domain.objects.exclude(tenant__schema_name="public")
            .select_related("tenant")
            .all(),
            "domain": settings.DOMAIN,
        },
    )


def franchise_list(request):
    franchises = Franchise.objects.filter(client=request.user) if request.user.user_type == User.FRANCHISE else Franchise.objects.all()
    return render(
        request, "franchises/franchises_list.html", {"franchises": franchises}
    )


#@verify_position(allowed_positions=[User.FRANCHISE])
def dump_data(request, franchise_id=1):
    """
    Función que permite obtener un backup de los datos de la empresa a un cliente
    :param request:
    :param franchise_id:
    :return:
    """
    import sys
    from io import StringIO

    from django.http import HttpResponse
    from django.core.management import call_command
    from django.db import connection

    from franchises.models import Franchise

    franchise_backup = StringIO()

    try:
        franchise = Franchise.search(franchise_id)
        if franchise:
            connection.set_tenant(franchise)
            sysout = sys.stdout
            sys.stdout = franchise_backup
            call_command(
                "dumpdata","users", indent=4#, exclude=["auth", "sessions", "contenttypes"]
            )
            sys.stdout = sysout
            connection.set_schema_to_public()
        else:
            messages.error(
                request, "Error al generar el archivo, por favor intente nuevamente."
            )
            return redirect("franchise_list")

    except Exception:
        messages.error(
            request, "Error al generar el archivo, por favor intente nuevamente."
        )
        return redirect("franchise_list")

    franchise_backup.seek(0)
    response = HttpResponse(franchise_backup, content_type="application/text")
    franchise_backup.close()
    response["Content-Disposition"] = (
        "attachment; filename=backup-%s.json" % franchise.name
    )

    return response