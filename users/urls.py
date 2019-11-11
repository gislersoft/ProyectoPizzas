from django.conf.urls import url
from .views import *

from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', user_profile, name='user_profile'),
    path("settings/", user_settings, name="user_settings"),
    url(r"^list", UsersList.as_view(), name="users_list"),
    path('clients_list/', clients_list, name='clients_list'),
]
