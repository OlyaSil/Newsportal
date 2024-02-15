import logging
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_apscheduler.models import DjangoJobExecution
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from news_portal.news.models import *
logger = logging.getLogger(__name__)

@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

def send_articles_to_subscribers():
    subscribers = Subscription.objects.all()

    for subscriber in subscribers:
        latest_articles = Post.objects.filter(
            timedate__gt=subscriber.last_delivery_time
        ).order_by('-timedate')[:5]

        # Формирование сообщения
        subject = 'Новые статьи на нашем сайте'
        message = render_to_string('email/articles_email.html', {'articles': latest_articles})
        plain_message = strip_tags(message)
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(subject, plain_message, from_email, [subscriber.email], html_message=message)

        subscriber.last_delivery_time = timezone.now()
        subscriber.save()

class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            send_articles_to_subscribers,
            trigger=CronTrigger(second="*/10"),
            id="send_articles_to_subscribers",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'send_articles_to_subscribers'.")

        scheduler.add_job(
            send_articles_to_subscribers,
            trigger=CronTrigger(day_of_week="fri", hour="18", minute="00"),
            id="send_articles_to_subscribers",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'send_articles_to_subscribers'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
