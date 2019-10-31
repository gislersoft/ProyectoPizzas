from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import *


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ("name", "image")
