from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Team) 
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation', 'created_date']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation', 'created_date']

