from django.conf.urls import url
from .views import *

urlpatterns = [url(r"^$", Start, name="inicio"), url(r"^$", Start, name="home")]
