from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Car
from rest_framework import permissions, viewsets
from .serializers import CarSerializer



class DashboardView(generic.ListView):
    template_name = "digitaltwin/dashboard.html"
    queryset = Car.objects.all()


class CarList(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
