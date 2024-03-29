from django.shortcuts import render
from .models import Car, Calendar, ChargeTimeScores
from rest_framework import permissions, viewsets
from .serializers import CarSerializer, CalendarSerializer, ChargeTimeScoresSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.db.models.functions import Now
from django.db.models import F, ExpressionWrapper, fields
import json

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

    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)

        except Car.DoesNotExist:
            return Response({'message': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)


        try:
            percentage = self.request.GET.get('battery_percentage', None)

            if percentage != None:
                car.battery_percentage = int(percentage)
                car.save()
        except:
            return Response({'message': 'Could not update value'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChargeScoresView(APIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = ChargeTimeScores


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        closest_entry = queryset.first()

        deadline = self.request.GET.get('deadline', 5)
        hours = self.request.GET.get('hours', 5)

        print(hours)

        if closest_entry:
            # Serialize the object
            serializer = ChargeTimeScoresSerializer(closest_entry, context={'request': request})
            # Return a Response object with the serialized data



            data = serializer.data
            data['best_options'] = find_best_options(data['scores'], int(deadline), int(hours))

            car = Car.objects.get(id=1)

            if (data['best_options'][0] == True):
                car.charge_state = 'charging'
            else:
                car.charge_state = 'not charging'



            car.save()


            return Response(data)
        else:
            return Response({'message': 'No entries found'}, status=404)

    def get_queryset(self):
        from django.db.models.functions import Now
        from django.db.models import ExpressionWrapper, fields, F
        from datetime import datetime

        # Current date and time
        now = Now()

        # Annotate queryset with the difference between "day" and the current date
        queryset = ChargeTimeScores.objects.annotate(
            diff=ExpressionWrapper(
                now - F('day'),
                output_field=fields.DurationField()
            )
        ).filter(
            # Optional: filter out future dates, if you only want past dates
            day__lte=now
        ).order_by('diff')

        return queryset


def find_best_options(options, deadline, hours):
    # Assuming options is a list of integers, convert it to integers if it's in string format
    options_list = [int(x) for x in options.split(',')][:deadline]
    
    # Sort the options list to find the lowest [hours] amount of numbers
    sorted_options = sorted(options_list)
    
    # Get the threshold value which is the highest among the lowest [hours] numbers
    if hours < len(sorted_options):
        threshold = sorted_options[hours-1]
    else:
        # In case hours is greater than or equal to the number of available options
        threshold = sorted_options[-1]

    # Create a boolean mask for the original list
    boolean_mask = [x <= threshold for x in options_list]

    positives = 0
    
    for (index, item) in enumerate(boolean_mask):
        if item == True:
            positives += 1
        
        if positives > hours:
            boolean_mask[index] = False



    # If the boolean mask is shorter than 24, extend it with False values
    boolean_mask.extend([False] * (24 - len(boolean_mask)))

    return boolean_mask


import requests

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


        url = "https://v1.nocodeapi.com/matser/calendar/SzYJsNehqZHCbDKv/listEvents"
        params = {}
        r = requests.get(url=url, params=params)
        result = r.json()
        Calendar.objects.create(google_response=result)


class CarList(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
