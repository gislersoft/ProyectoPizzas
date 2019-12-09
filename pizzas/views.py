from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from pizzas.forms import ToppingForm
from pizzas.models import Topping
from pizzas.forms import PizzaForm
from pizzas.models import Pizza


def pizzas_list(request):
    pizzas_list2 = Pizza.objects.all()
    lista = []
    for i in list(pizzas_list2):
        lista.append({"id": i.id, "toppings": list(i.toppings.all())})
    context = {"pizzas": list(pizzas_list2), "toppings_map": lista}
    return render(request, "pizzas_list.html", context)


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
            messages.success(request, "Ingrediente guardado correctamente.")
            return redirect("pizzas_management")
        else:
            messages.error(request, "Por favor revise los campos en rojo")
    return render(
        request,
        "pizzas/topping_management.html",
        {"form": form, "toppings": Topping.objects.all()},
    )


def pizzas_management(request, pizza_id=None):
    if pizza_id:
        pizza = get_object_or_404(Pizza, id=pizza_id)
    else:
        pizza = None

    form = PizzaForm(instance=pizza)
    pizzas = Pizza.objects.all()
    pizza_toppings = []
    for pizza in pizzas:
        pizza_toppings.append({"id": pizza.id, "toppings": list(pizza.toppings.all())})
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            if pizza_id:
                obj = Pizza.objects.get(pk=pizza_id)
            else:
                obj = Pizza()  # gets new object
            obj.name = form.cleaned_data["name"]
            obj.image = form.cleaned_data["image"]
            obj.price = form.cleaned_data["price"]
            obj.toppings.set(form.cleaned_data["toppings"])
            obj.save()
            messages.success(request, "Pizza guardada correctamente.")
            return redirect("pizzas_management")
        else:
            messages.error(request, "Por favor revise los campos en rojo")
    return render(
        request,
        "pizzas/pizzas_management.html",
        {
            "form": form,
            "toppings_list": Topping.objects.all(),
            "pizzas": pizzas,
            "pizza_toppings": pizza_toppings,
        },
    )
