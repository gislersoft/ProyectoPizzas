from django.shortcuts import render

from franchises.models import Plan


def Start(request):
    # User.initial_user()
    if request.tenant.schema_name == "public":
        return render(
            request,
            "public_view/public_init.html",
            {"title": "Inicio", "plans": Plan.objects.all()},
        )

    return render(request, "public_view/public_init.html", {"title": "Inicio"})


def franchise_unavailable(request):
    return render(request, "public_view/franchise_unavailable.html")
