from django.contrib import admin
from .models import *
# Register your models here.
class CeleryTaskHechasAdmin(admin.ModelAdmin):
    model = CeleryTaskHechas
    list_display = ['celular','fechayhora']

admin.site.register(CeleryTaskHechas,CeleryTaskHechasAdmin)