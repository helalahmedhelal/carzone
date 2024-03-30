from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_title', 'state', 'city', 'price', 'is_featured', 'created_date']
    search_fields = ['car_title', 'state', 'city', 'model']
    list_filter = ['state', 'condition', 'is_featured', 'created_date']

