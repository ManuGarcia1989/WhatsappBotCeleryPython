from django.contrib import admin
from .models import difusion

# Register your models here.

class difusionAdmin(admin.ModelAdmin):
    list_display = ['texto']

admin.site.register(difusion, difusionAdmin)