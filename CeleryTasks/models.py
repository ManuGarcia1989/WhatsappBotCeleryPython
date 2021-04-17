from django.db import models
from datetime import datetime
# Create your models here.

class CeleryTaskHechas (models.Model):
    celular = models.CharField(max_length=80,unique=True)
    fechayhora = models.DateTimeField(default= datetime.now())