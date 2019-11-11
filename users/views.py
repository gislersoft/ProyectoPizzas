import os
from django.contrib import messages
from django.views.generic import (
    ListView
)
from .models import User

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm, UserProfileForm


# Create your views here.
def clients_list(request):
    users = User.objects.filter(user_type="CLIENT")
    contexto = {'users': users}
    return render(request, 'clients_list.html', contexto)


def home(request):
    return render(request, 'home_test.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = User.FRANCHISE if request.tenant.schema_name == "public" else User.CLIENT
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


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

    return render(
        request,
        "user_profile.html",
        {"form": form},
    )


def dashboard(request):
    return render(
        request,
        "base.html",
    )


def user_settings(request):
    def get_list_of_files(dir_name):
        # create a list of file and sub directories
        # names in the given directory
        list_of_file = os.listdir(dir_name)
        all_files = list()
        # Iterate over all the entries
        for entry in list_of_file:
            # Create full path
            full_path = os.path.join(dir_name, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(full_path):
                all_files = all_files + get_list_of_files(full_path)
            else:
                all_files.append(full_path)
        return all_files

    static_theme_css_directory = './static/css/themes';
    # Get the list of all files in directory tree at given path
    list_of_files = get_list_of_files(static_theme_css_directory)

    # Transform the list of files to a list of readable names.
    # returning name,path to file
    def transform_name(x):
        x = x.replace('./static/css/themes', '')
        original_file = x
        x = x.replace('.min.cs', '')
        x = x.replace('\\', '-')
        x = x.replace('-', ' ')
        x = x.replace('-', ' ')
        x = x.strip()
        x = x.title()
        return x + "," + original_file

    list_themes = list(filter(lambda x: ".min.cs" in x, list_of_files))
    list_themes = list(map(transform_name, list_themes))

    all_themes = []

    for theme in list_themes:
        info = theme.split(",")
        all_themes.append({
            "name": info[0],
            "value": info[1]
        })

    return render(
        request, "user_settings.html", {"list_of_css_themes": all_themes}
    )
