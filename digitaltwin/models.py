from django.db import models
from django.core.validators import int_list_validator

# Create your models here.


class Calendar(models.Model):

    google_response = models.JSONField()


class ChargeTimeScores(models.Model):
    day = models.DateField(unique=True)
    scores = models.CharField(
        validators=[int_list_validator], max_length=200, default=""
    )


class Car(models.Model):
    # Assuming you want at least the name for the car, you can add more fields as needed

    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=8, default="")
    battery_percentage = (
        models.IntegerField()
    )  # Representing battery level as an integer (e.g., percentage)
    charge_state = models.CharField(
        max_length=100
    )  # e.g., "charging", "discharging", "full"
    car_state = models.CharField(max_length=100)  # e.g., "connected", "plugged_in"

    estimated_time_until_full = models.DurationField()

    charge_target_hours = models.IntegerField(default=5)

    # Automatically updates to current date and time on save
    last_update = models.DateTimeField(auto_now=True)
    calendar_offset = models.IntegerField(default=3)


class Counter(models.Model):
    count = models.IntegerField(default=0)
