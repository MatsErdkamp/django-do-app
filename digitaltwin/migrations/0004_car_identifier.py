# Generated by Django 4.0.3 on 2024-03-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitaltwin', '0003_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='identifier',
            field=models.CharField(default='', max_length=8),
        ),
    ]