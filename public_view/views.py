from django.shortcuts import render

from franchises.models import Plan
from pizzas.models import Pizza


def Start(request):
    # User.initial_user()
    if request.tenant.schema_name == "public":
        return render(
            request,
            "public_view/public_init.html",
            {"title": "Inicio", "plans": Plan.objects.all()},
        )
    pizzas_list2 = Pizza.objects.all()
    lista = []
    for i in list(pizzas_list2):
        lista.append({"id": i.id, "toppings": list(i.toppings.all())})


    return render(request, "public_view/public_init.html",
                  {"title": "Inicio",
                   "pizzas": list(pizzas_list2),
                   "toppings_list": lista})






def franchise_unavailable(request):
    return render(request, "public_view/franchise_unavailable.html")
