# -*- coding: utf-8 -*-
#!/usr/Scripts/python3
import sys
import os
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from .tasks import enviar_libre_tarea
from django.db import models

# Create your models here.

class difusion(models.Model):
    texto = models.TextField(max_length=2000,blank= True,null=True, verbose_name="Texto del mensaje")
    archivo = models.FileField(verbose_name="Archivo",upload_to="mensaje_libre", blank=True, null=True)
    adjunto = models.BooleanField(default=False)

    def __str__(self):
        return "%s,%s,%s" % (str(self.texto),str(self.archivo),str(self.adjunto))


@receiver(post_save, sender= difusion)
def crear_mensaje_libre(sender, instance, created, **kwargs):
    llego = str(instance)
    cadena = llego.split(',')
    if created:
        print("ENVIANDO LA TAREA")
        enviar_libre_tarea.delay(cadena)
        print("SI ENVIO LA TAREA")