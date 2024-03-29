"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.views.static import serve
from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
from digitaltwin.views import CarList, CalendarView, ChargeScoresView, CarUpdateView
import os
from .settings import BASE_DIR
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r"car", CarList)

router.register(r"calendar", CalendarView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path("api/curve/", ChargeScoresView.as_view(), name='random-numbers'),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("", TemplateView.as_view(template_name="index.html")),
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html"), name="app"),
]
