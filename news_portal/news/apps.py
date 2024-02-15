from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals

red = redis.Redis(
    host='redis-13480.c299.asia-northeast1-1.gce.cloud.redislabs.com',
    port=13480,
    password='mJpdPY526BL2DNporPeZpJwK50EQ584z'
)