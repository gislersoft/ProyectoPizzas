from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^registrar-solicitud/(?P<plan_id>\d+)$",
        register_franchise, name="franchise_register_franchise"),
    url(r"^registrar-solicitud",
        register_franchise, name="franchise_register_franchise"),

    #url(r"^edit-plans$", edit_plans, name="franchise_edit_plans_franchise"),
]
