from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password
from .forms import *
from .models import *
from django.views.generic import ListView
from utils.decorators import auth_check_msg

from .forms import SignUpForm, UserProfileForm


@auth_check_msg(users=(User.ADMINISTRATOR,))
def clients_list(request):
    users = User.objects.filter(user_type="CLIENT")
    context = {"users": users}
    return render(request, "clients_list.html", context)


def home(request):
    return render(request, "home_test.html")



def signup(request,user_type='general'):
    if request.method == 'POST':
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
            if user_type == 'admin':
                return user, redirect('home')
            else:
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


@auth_check_msg(users=(User.ADMINISTRATOR,))
def register_user_admin(request):
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
        {
            "form": form,
            "title": "User registration",
            "domain": settings.DOMAIN,
            "users": User.objects.all(),
        },
    )


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
    return render(request, "dashboard.html")
