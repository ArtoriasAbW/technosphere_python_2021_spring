import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

app = Celery('application', include=['application.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-me-every-second': {
        'task': 'application.tasks.hello',
        'schedule': 60.0 * 5
    }
}
