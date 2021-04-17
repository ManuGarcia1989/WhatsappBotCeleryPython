# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals, absolute_import, print_function
import os
from celery import Celery
from django.conf import settings
from django.apps import apps
# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FemputadoraDesktop.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('FemputadoraDesktop')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#app.conf.update(
#    BROKER_URL = 'redis://localhost:6379/0', #Nota 4
#)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))