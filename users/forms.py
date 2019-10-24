from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Necesario. 100 caracteres o menos.', label="Nombre")
    last_name = forms.CharField(max_length=100, help_text='Necesario. 100 caracteres o menos.', label="Apellido")
    email = forms.CharField(max_length=100, help_text='Necesario. 100 caracteres o menos.')
    password2 = forms.CharField(help_text='Introduce la misma contraseña para verificación.', label="Confirmar contraseña", widget=forms.PasswordInput())
    password1 = forms.CharField(help_text='Introduce tu contraseña.', label="Contraseña", widget=forms.PasswordInput())

    class Meta:
        model = User
        #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        fields = ('email', 'first_name', 'last_name')