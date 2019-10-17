from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from franchises.forms import PlanForm
from franchises.models import Plan, Module


def plan_management(request, plan_id=None):
    if plan_id:
        plan = get_object_or_404(Plan, id=plan_id)
    else:
        plan = None
    Module.initual_modules()
    form = PlanForm(instance=plan)

    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan guardado correctamente")
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(request, "pizzas/plan_management.html", {'form':form})