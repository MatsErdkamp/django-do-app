# Generated by Django 4.0.3 on 2024-04-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitaltwin', '0008_car_car_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='charge_target_hours',
            field=models.IntegerField(default=5),
        ),
    ]
