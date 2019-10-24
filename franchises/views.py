from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from franchises.forms import PlanForm
from franchises.models import Plan, Module
from django.conf import settings
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from .forms import *
from .models import *
from SuperPizzas.utils import verify_position


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
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(
        request,
        "franchises/plan_management.html",
        {"form": form, "plans": Plan.objects.all()},
    )


# @verify_position(allowed_position=["Administrador"])
def register_franchise(request, plan_id=1):
    plan = Plan.search(plan_id)
    if not plan:
        messages.error(request, "No existe el plan buscado")
        return redirect("inicio")

    if request.method == "POST":

        form = FranchiseForm(request.POST)

        if form.is_valid():

            franchise = form.save()
            domain = Domain(
                domain=f"{franchise.schema_name}.{settings.DOMAIN}",
                is_primary=True,
                tenant=franchise,
            )
            domain.save()
            # connection.set_tennant(franchise)
            User.initial_user(franchise.client)
            connection.set_schema_to_public()

            franchise.plan = plan
            franchise.save()
            messages.success(request, "La franquicia ha sido creada exitosamente")
            return redirect("franchise_register_franchise")
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
