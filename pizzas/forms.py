from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import *


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ("name", "image")


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ("name", "image", "price", "toppings")
        widgets = {"toppings": forms.CheckboxSelectMultiple}
