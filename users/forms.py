from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    last_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    email = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')

    class Meta:
        model = User
        #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        fields = ('email', 'first_name', 'last_name')