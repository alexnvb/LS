from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', "tel")
    list_display_links = ('id', 'name')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'plate_number')
    list_display_links = ('id', 'name')

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'tel')
    list_display_links = ('id', 'name')

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'date_created', 'date_appointed',
                    'contractor', 'city', 'vehicle', 'done')
    list_display_links = ('id', 'type')