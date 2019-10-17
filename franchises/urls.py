from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import *

urlpatterns = [
    path('plan-management/', plan_management, name="plan_management"),
    path('plan-management/<int:plan_id>', plan_management, name="plan_management"),
]
