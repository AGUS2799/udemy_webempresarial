from email.policy import default
import django
from django.apps import AppConfig
from django.contrib import admin
from .models import Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')


admin.site.register(Services, ServicesAdmin)