from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from pizzas.forms import ToppingForm
from pizzas.models import Topping


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
