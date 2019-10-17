from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView
)
from .models import User

# Create your views here.
class ListarUsuarios(ListView):
    model = User
    template_name = "listado.html"
    context_object_name = "lista_usuario"

    def dispatch(self, request, *args, **kwargs):
        return super(ListarUsuarios, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListarUsuarios, self).get_context_data(**kwargs)
        context["titulo"] = "Listado de usuarios"
        context["lista_encabezados"] = [
            "Email",
            "Nombre completo",
            "Es staff",
            "Estado",
            "Fecha de Activación",
            "Opciones",
        ]

        return context
