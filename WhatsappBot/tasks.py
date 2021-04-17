# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# Create your tasks here
from __future__ import unicode_literals
import os
from django.contrib import admin

from celery import shared_task
import FemputadoraDesktop.apiconection as api


r = api.API()



@shared_task
def enviar_libre_tarea(cadena):
    print ("ENTRA A LA TAREA ENVIAR MENSAJE LIBRE\n")
    texto = cadena[0]
    archivo = cadena[1]
    adjunto = cadena[2]
    print("%s %s %s" %(texto,archivo,adjunto))
    r.Libre(texto,archivo,adjunto)