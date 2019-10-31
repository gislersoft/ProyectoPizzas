from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path("topping-management/", topping_management, name="topping_management"),
    path("topping-management/<int:plan_id>", topping_management, name="topping_management"),
]
