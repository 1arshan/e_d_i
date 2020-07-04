"""import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adcbackend.settings')

app = Celery('adcbackend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
"""