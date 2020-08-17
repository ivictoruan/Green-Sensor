from django.contrib import admin
from .models import Buildings
# Register your models here.

@admin.register(Buildings)
class BuildingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_devices']
