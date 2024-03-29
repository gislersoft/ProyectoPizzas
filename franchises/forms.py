from django import forms
from django_select2.forms import Select2MultipleWidget



from .models import *


class FranchiseForm(forms.ModelForm):

    #,public_key='6Lc68b8UAAAAAClNVCXOXe3iedRGpkaOt_dyOIC-',
    #private_key='6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')
    def __init__(self, *args, **kwargs):
        from django.conf import settings

        super(FranchiseForm, self).__init__(*args, **kwargs)
        self.fields["schema_name"].label = "Subdominio"
        self.fields[
            "schema_name"
        ].help_text = f"Esta será su dirección: subdominio.{settings.DOMAIN}"
        # self.fields["client"].queryset = self.fields["client"]\
        #    .queryset.filter(position="Client")

    class Meta:
        model = Franchise
        fields = ("name", "schema_name", "validity")
        widgets = {
            "validity": forms.DateInput(
                attrs={"class": "component-date"}, format="%Y-%m-%d"
            )
        }

    def clean(self):
        form_data = self.cleaned_data
        tenant_address = form_data["schema_name"]
        if tenant_address.lower() == "www":
            self._errors["schema_name"] = [
                f"No es posible registrar {tenant_address} como dirección de correo válida"
            ]
        try:
            Franchise.objects.get(schema_name=tenant_address)
            self._errors["schema_name"] = [
                f"Ya existe una franquicia con el nombre {tenant_address}"
            ]
        except:
            pass

        franchise_name = form_data["name"]
        try:
            Franchise.objects.get(name=franchise_name)
            self._errors["nombre"] = [
                f"Ya existe una franquicia con el nombre {tenant_address}"
            ]
        except:
            pass


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = ("theme", "color")


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ("name", "description", "price", "modules", "max_users")
        widgets = {"modules": Select2MultipleWidget()}
