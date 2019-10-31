from django.views.generic import (
    ListView
)
from .models import User

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'home_test.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('home_test')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', { 'form' : form })

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
