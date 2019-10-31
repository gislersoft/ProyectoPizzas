from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [path("franchise-unavailable", franchise_unavailable, name="franchise_unavailable"),
               url(r"^$", Start, name="inicio"), url(r"^$", Start, name="home")]
