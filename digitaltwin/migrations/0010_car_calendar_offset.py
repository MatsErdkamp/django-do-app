# Generated by Django 5.0 on 2024-04-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("digitaltwin", "0009_car_charge_target_hours"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="calendar_offset",
            field=models.IntegerField(default=3),
        ),
    ]
