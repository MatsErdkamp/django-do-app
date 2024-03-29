from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from digitaltwin.models import Counter, Car
from .serializers import CarSerializer
import json

@receiver(post_save, sender=Car)
@receiver(post_delete, sender=Car)
def car_updated(sender, instance, **kwargs):
    """
    Signal handler to be called whenever a Counter object is saved or deleted.
    """

    channel_layer = get_channel_layer()
    group_name = 'car_updates'

    serialized_car = CarSerializer(instance).data
    
    # Asynchronously send the update to the group
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'car_update',
            'car': serialized_car
        }
    )





@receiver(post_save, sender=Counter)
@receiver(post_delete, sender=Counter)
def counter_updated(sender, instance, **kwargs):
    """
    Signal handler to be called whenever a Counter object is saved or deleted.
    """

    channel_layer = get_channel_layer()
    group_name = 'counter_updates'
    
    # Asynchronously send the update to the group
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'count_update',
            'count': instance.count if instance else 0
        }
    )