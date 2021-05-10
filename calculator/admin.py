from django.contrib import admin
from calculator.models import Weight, Height, BmiCalculate
# Register your models here.
@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display=('weight_range', 'weight_measure')

@admin.register(Height)
class HeightAdmin(admin.ModelAdmin):
    list_display=('height_range', 'height_measure',)

@admin.register(BmiCalculate)
class BmiCalculateAdmin(admin.ModelAdmin):
    list_display=('user', 'weight', 'height')