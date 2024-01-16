import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'msg_every_mon_morning': {
        'task': 'news.tasks.sub_pub_notification',
        'schedule': crontab(), #hour=8, minute=0, day_of_week='monday'
    },
}