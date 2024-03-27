from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

app = Celery('news_portal')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-weekly-newsletter': {
        'task': r'C:\Users\olsil\PycharmProjects\NewsPortal\news_portal\news\tasks.py',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
    },
}

if __name__ == '__main__':
    app.start()
