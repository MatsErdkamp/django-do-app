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
from digitaltwin.views import CarList
import os
from .settings import BASE_DIR


router = routers.DefaultRouter()
router.register(r'car', CarList)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^dashboard/$', lambda request: serve(request, 'index.html', os.path.join(BASE_DIR, 'digital-frontend/dist'))),
    re_path(r'^dashboard/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'digital-frontend/dist')}),
]

