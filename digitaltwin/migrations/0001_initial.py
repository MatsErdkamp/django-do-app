# Generated by Django 4.0.3 on 2024-03-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('battery_percentage', models.IntegerField()),
                ('charge_state', models.CharField(max_length=100)),
                ('estimated_time_until_full', models.DurationField()),
            ],
        ),
    ]
