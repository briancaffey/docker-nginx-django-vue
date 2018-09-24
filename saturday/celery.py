import os
from celery import Celery
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saturday.settings')

app = Celery('saturday')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    time.sleep(5)
    print("Weeeee")