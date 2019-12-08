from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path("topping-management/", topping_management, name="topping_management"),
    path(
        "topping-management/<int:topping_id>",
        topping_management,
        name="topping_management",
    ),
    path(
        "pizzas-management/<int:plan_id>", pizzas_management, name="pizzas_management"
    ),
    path("pizzas-management/", pizzas_management, name="pizzas_management"),
    path('pizzas_list/', pizzas_list, name='pizzas_list'),
]
