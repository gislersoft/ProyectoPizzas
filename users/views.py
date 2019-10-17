from django.shortcuts import render

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