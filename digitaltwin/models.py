from django.db import models

# Create your models here.


class Calendar(models.Model):

    google_response = models.JSONField()


class Car(models.Model):
    # Assuming you want at least the name for the car, you can add more fields as needed
    
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=8, default='')
    battery_percentage = (
        models.IntegerField()
    )  # Representing battery level as an integer (e.g., percentage)
    charge_state = models.CharField(
        max_length=100
    )  # e.g., "charging", "discharging", "full"
    estimated_time_until_full = (
        models.DurationField()
    )


class Counter(models.Model):
    count = models.IntegerField(default=0)
