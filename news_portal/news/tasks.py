from celery import shared_task
from django.core.mail import send_mail
from .models import Subscription, Post
from datetime import timedelta
from django.utils import timezone

@shared_task
def send_notification_to_subscribers(news_id):
    news = Post.objects.get(id=news_id)
    subscribers = Subscription.objects.all()

    for subscriber in subscribers:
        send_mail(
            'Новая новость',
            f'Появилась новая новость: {news.title}',
            'silakova-o.a@yandex.ru',
            [subscriber.email],
            fail_silently=False,
        )

@shared_task
def send_weekly_newsletter():
    last_week = timezone.now() - timedelta(days=7)
    latest_news = Post.objects.filter(created_at__gte=last_week)
    subscribers = Subscription.objects.all()

    for subscriber in subscribers:
        send_mail(
            'Еженедельная рассылка',
            'Список последних новостей: {}'.format(
                ', '.join([news.title for news in latest_news])
            ),
            'silakova-o.a@yandex.ru',
            [subscriber.email],
            fail_silently=False,
        )