from django.shortcuts import render
from .models import Car, Calendar
from rest_framework import permissions, viewsets
from .serializers import CarSerializer, CalendarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random


class CarUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Car.objects.all()

    def post(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({'message': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RandomNumbersView(APIView):

    queryset = Calendar.objects.all()  # REPLACE
    """
    API endpoint that returns a list of 24 random numbers between 0 and 100.
    """
    def get(self, request, *args, **kwargs):
        # Generate a list of 24 random numbers between 0 and 100
        random_numbers = [random.randint(0, 100) for _ in range(24)]
        
        # Return the list as a JSON response
        return Response(random_numbers, status=status.HTTP_200_OK)



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
