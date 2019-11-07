from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.views.generic import ListView
from django.contrib.auth.hashers import make_password


def register_user_admin(request):
    # TODO: Check if user is admin
    # if not request.user.is_authenticated:
    #     messages.error(
    #         request, f"Debes iniciar sesión."
    #     )
    #     return redirect("home")
    # if request.user.user_type=="Administrador":
    if request.method == "POST":

        form = UserForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, "El usuario ha sido creada exitosamente")
            return redirect("register_user_admin")
        else:
            messages.error(
                request, "No se pudo registrar al usuario, contacte al soporte"
            )
    else:
        form = UserForm()

    return render(
        request,
        "users/register_user_admin.html",
        {"form": form, "title": "User registration", "domain": settings.DOMAIN},
    )
    # else:
    #     messages.error(
    #         request, f"Como {request.user.user_type} no puedes acceder a esta página."
    #     )
    #     return redirect("home")


class UsersList(ListView):
    model = User
    template_name = "user_list_template.html"
    context_object_name = "users_list"

    def dispatch(self, request, *args, **kwargs):
        return super(UsersList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersList, self).get_context_data(**kwargs)
        context["title"] = "Listado de usuarios"
        context["headers_list"] = [
            "Email",
            "Nombre completo",
            "Es staff",
            "Estado",
            "Fecha de Activación"
        ]
        return context
