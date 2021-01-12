from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings',  namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, debug_task.s(), name='add every 10')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
