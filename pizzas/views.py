from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from pizzas.forms import ToppingForm
from pizzas.models import Topping
from pizzas.forms import PizzaForm
from pizzas.models import Pizza


def topping_management(request, plan_id=None):
    if plan_id:
        topping = get_object_or_404(Topping, id=plan_id)
    else:
        topping = None

    form = ToppingForm(instance=topping)

    if request.method == "POST":
        form = ToppingForm(request.POST, request.FILES, instance=topping)
        if form.is_valid():
            form.save()
            messages.success(request, "ingrediente guardado correctamente")
            form = ToppingForm()
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(
        request,
        "pizzas/topping_management.html",
        {"form": form, "toppings": Topping.objects.all()},
    )

def pizzas_management(request, plan_id=None):
    if plan_id:
        pizza = get_object_or_404(Pizza, id=plan_id)
    else:
        pizza = None

    form = PizzaForm(instance=pizza)

    if request.method == "POST":
        form = ToppingForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            messages.success(request, "pizza guardada correctamente")
            form = ToppingForm()
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(
        request,
        "pizzas/pizza_management.html",
        {"form": form, "pizzas": Pizza.objects.all()},
    )
