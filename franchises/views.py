from django.contrib import messages
from django.db import connection
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from SuperPizzas.utils import verify_position
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


@verify_position(allowed_positions=[User.FRANCHISE])
def register_franchise(request, plan_id=1):
    plan = Plan.search(plan_id)
    if not plan:
        messages.error(request, "No existe el plan buscado")
        return redirect("home")

    if request.method == "POST":
        form = FranchiseForm(request.POST)
        if form.is_valid():
            from django.db import connection
            franchise = form.save(commit=False)
            franchise.client = request.user
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
        else:
            messages.error(
                request, "No se pudo registrar la franquicia, contacte al soporte"
            )
    else:
        form = FranchiseForm()

    return render(
        request,
        "franchises/registry_franchises.html",
        {
            "form": form,
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
def dump_data(request, empresa_id):
    """
    Función que permite obtener un backup de los datos de la empresa a un cliente
    :param request:
    :param empresa_id:
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
        franchise = Franchise.search(empresa_id)
        if franchise:
            connection.set_tenant(franchise)
            sysout = sys.stdout
            sys.stdout = franchise_backup
            call_command(
                "dumpdata", indent=4, exclude=["auth", "sessions", "contenttypes"]
            )
            sys.stdout = sysout
            connection.set_schema_to_public()
        else:
            messages.error(
                request, "Error al generar el archivo, por favor intente nuevamente."
            )
            return redirect("empresa_gestionar_empresas_cliente")

    except Exception:
        messages.error(
            request, "Error al generar el archivo, por favor intente nuevamente."
        )
        return redirect("empresa_gestionar_empresas_cliente")

    franchise_backup.seek(0)
    response = HttpResponse(franchise_backup, content_type="application/text")
    franchise_backup.close()
    response["Content-Disposition"] = (
        "attachment; filename=backup-%s.json" % franchise.nombre
    )

    return response