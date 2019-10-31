from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from users.models import User
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
