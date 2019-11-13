from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from pizzas.forms import ToppingForm
from pizzas.models import Topping
from pizzas.forms import PizzaForm
from pizzas.models import Pizza


def topping_management(request, topping_id=None):
    if topping_id:
        topping = get_object_or_404(Topping, id=topping_id)
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
        form = PizzaForm(request.POST, request.FILES, instance=pizza)

        toppings = []
        topping_lists = request.POST.get("toppings", "").split(',')
        for topping_id in topping_lists:
            toppings.append(Topping.objects.get(pk=topping_id))

        if form.is_valid():
            obj = Pizza()  # gets new object
            obj.name = form.cleaned_data['name']
            obj.image = form.cleaned_data['image']
            obj.price = form.cleaned_data['price']
            obj.save();  # Save the pizza to get a new id.
            obj.toppings.set(toppings);  # Add the toppings
            obj.save();  # Save again.
            messages.success(request, "pizza guardada correctamente")
            form = PizzaForm()
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(
        request,
        "pizzas/pizzas_management.html",
        {"form": form, "toppings_list": Topping.objects.all()},
    )
