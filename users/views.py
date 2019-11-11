from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from .forms import *
from .models import *
from django.views.generic import ListView

from .forms import SignUpForm, UserProfileForm


def clients_list(request):
    users = User.objects.filter(user_type="CLIENT")
    contexto = {'users':users}
    return render(request, 'clients_list.html',contexto)

  
def home(request):
    return render(request, "home_test.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = (
                User.FRANCHISE
                if request.tenant.schema_name == "public"
                else User.CLIENT
            )
            user.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def register_user_admin(request):
    if not request.user.is_authenticated:
        messages.error(request, f"Debes iniciar sesión.")
        return redirect("login")
    if request.user.user_type == "Administrador":
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
    else:
        messages.error(
            request, f"Como {request.user.user_type} no puedes acceder a esta página."
        )
        return redirect("home")


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
            "Fecha de Activación",
        ]
        return context


def user_profile(request):
    form = UserProfileForm(instance=request.user)
    if request.user.email == "admin@admin.co":
        user = request.user
        user.user_type = User.ADMINISTRATOR
        user.save()
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente")
            form = UserProfileForm()
        else:
            messages.error(request, "Por favor revise los campos en rojo")

    return render(request, "user_profile.html", {"form": form})


def dashboard(request):
    return render(request, "base.html")
