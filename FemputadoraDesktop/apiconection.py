# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import unidecode
import time
import hashlib
import requests
import hmac
import smtplib
from .robot_whatsapp_email import *
from time import sleep
from CeleryTasks.models import CeleryTaskHechas

# from django.core import serializers


class API:
    url_whatsapp = "http://178.128.58.85/api/whatsapp"
    url_whatsapp_elite = "http://178.128.58.85/api/whatsapp_elite"
    wa = whatsapp()

    def Libre(self, texto, archivo, adjunto):
        self.wa.iniciar_whatsapp()
        consulta = requests.get(self.url_whatsapp_elite, timeout=30, verify=True).json()
        for fulano in consulta:
            nombre = str(fulano["nombre"])
            mensaje_ev = texto
            celular = ""
            try:
                celular = str(fulano['celular']).replace("."," ")
            except:
                celular = str(fulano['celular'])
            numero = "57" + celular
            print("%s %s %s"%(nombre,numero,mensaje_ev))
            try:
                celu = CeleryTaskHechas.objects.get(celular= celular)
            except:
                pinto = CeleryTaskHechas()
                pinto.celular = celular
                pinto.save()
                if adjunto == "False":
                    self.enviar_whatsapp(numero, mensaje_ev)
                else:
                    self.enviar_whatsapp_imagen(numero, mensaje_ev, archivo)



    def enviar_whatsapp(self, numero, mensaje):
        self.wa.enviarTexto(numero, mensaje)

    def enviar_whatsapp_imagen(self, numero, mensaje, dire):
        self.wa.enviarFoto(numero, mensaje, dire)