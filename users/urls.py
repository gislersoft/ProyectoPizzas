from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path("register-user-admin/", register_user_admin, name="register_user_admin")
]
