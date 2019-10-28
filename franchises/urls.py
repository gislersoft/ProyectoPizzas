from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path("plan-management/", plan_management, name="plan_management"),
    path("plan-management/<int:plan_id>", plan_management, name="plan_management"),
    url(
        r"^registrar-solicitud/(?P<plan_id>\d+)$",
        register_franchise,
        name="franchise_register_franchise",
    ),
    url(
        r"^registrar-solicitud", register_franchise, name="franchise_register_franchise"
    ),
]
