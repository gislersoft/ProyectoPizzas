from django import forms
from django_select2.forms import Select2MultipleWidget

from .models import *

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ("name", "price", "modules", "max_users")
        widgets = {"modules": Select2MultipleWidget()}
