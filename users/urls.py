from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^listar$", UsersList.as_view(), name="users_list"),
]
