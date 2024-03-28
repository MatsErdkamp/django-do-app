from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Car, Calendar
from rest_framework import permissions, viewsets
from .serializers import CarSerializer, CalendarSerializer


class CalendarView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()

    def get_queryset(self):
        """
        This method checks if the Calendar queryset is empty.
        If it is, it makes an API call to fetch calendar data and creates Calendar objects.
        """
        queryset = Calendar.objects.all()
        if not queryset.exists():
            self.fetch_and_create_calendar_data()
            queryset = Calendar.objects.all()  # Re-fetch the queryset after creation
        return queryset

    def fetch_and_create_calendar_data(self):
        import requests

        url = "https://v1.nocodeapi.com/matser/calendar/SzYJsNehqZHCbDKv/listEvents"
        params = {}
        r = requests.get(url=url, params=params)
        result = r.json()
        Calendar.objects.create(google_response=result)


class CarList(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
