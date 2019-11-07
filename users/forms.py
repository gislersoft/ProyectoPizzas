from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       AuthenticationForm)
from .models import User
from django_select2.forms import Select2MultipleWidget

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "avatar",
            "user_type",
        )
        widgets = {"password": forms.PasswordInput}

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


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


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar')
