"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path

from .views import error_404_view, dashboard_view, root_view
from pms.views import pms_home_to_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", root_view, name="root"),
    path("dashboard/", dashboard_view, name="dashboard"),
    #
    path("pms", pms_home_to_redirect), 
    path("pms/", include("pms.urls", namespace="pms")),
] + [
    re_path(r"^", error_404_view, name="error_404")
]
