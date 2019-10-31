from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Necesario. 100 caracteres o menos.', label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, help_text='Necesario. 100 caracteres o menos.', label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, help_text='Necesario. 100 caracteres o menos.', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(help_text='Introduce la misma contraseña para verificación.', label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text='Introduce tu contraseña.', label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        fields = ('email', 'first_name', 'last_name')