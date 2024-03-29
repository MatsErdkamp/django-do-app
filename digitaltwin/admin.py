from django.contrib import admin
from .models import Car, Counter, ChargeTimeScores
# Register your models here.


admin.site.register(Car)
admin.site.register(ChargeTimeScores)

admin.site.register(Counter)
