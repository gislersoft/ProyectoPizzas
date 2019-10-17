from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from users.models import User
from franchises.models import Plan


def end_sessions(request):
    evento = Evento.obtener_evento_sesion(request)
    participante = Usuario.obtener_participante_sesion(request)
    if evento:
        del request.session["id_evento"]
    if participante:
        del request.session["id_participante"]


# Create your views here.
def Start(request):
    # User.initial_user()
    if request.tenant.schema_name == "public":
        return render(
            request,
            "public_view/public_init.html",
            {"title": "Inicio", "plans": Plan.objects.all()},
        )
    else:
        end_sessions(request)

    return render(request, "vista_publica/inicio.html", {"title": "Inicio"})
