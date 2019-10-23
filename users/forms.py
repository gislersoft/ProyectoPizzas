from django import forms
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
