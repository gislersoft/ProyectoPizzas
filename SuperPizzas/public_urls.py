"""SuperPizzas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

#Test
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name ="base.html"), name="home"),
    path("test-base", TemplateView.as_view(template_name ="base.html"), name="test_base"),
    path("test-table", TemplateView.as_view(template_name ="tables_base.html"), name="test_table"),
    path("test-landing", TemplateView.as_view(template_name ="landing_base.html"), name="test_landing"),
    url(r"^users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
