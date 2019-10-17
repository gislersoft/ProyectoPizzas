from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^listar$", ListarUsuarios.as_view(), name="users_listado"),
]
