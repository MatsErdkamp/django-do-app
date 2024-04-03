from rest_framework import serializers
from .models import Car, Calendar, ChargeTimeScores
from datetime import timedelta

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'identifier', 'battery_percentage', 'charge_state','car_state', 'charge_target_hours', 'estimated_time_until_full']

    def update(self, instance, validated_data):
        instance.battery_percentage = validated_data.get('battery_percentage', instance.battery_percentage)
        
        # Calculate estimated time until full charge
        percentage_needed = 100 - instance.battery_percentage
        hours_until_full = percentage_needed // 10
        instance.estimated_time_until_full = timedelta(hours=hours_until_full)
        
        # # Update charge state based on new battery percentage
        # if instance.battery_percentage >= 100:
        #     instance.charge_state = 'full'
        # else:
        #     instance.charge_state = 'charging'

        instance.save()
        return instance


class ChargeTimeScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeTimeScores
        fields = "__all__"


class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"
