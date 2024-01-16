import datetime

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPaper import settings
from news.models import Post, Category


@shared_task
def sub_pub_notification():
    day = datetime.datetime.now()
    last_week = day - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_of_creation__gte=last_week).order_by('time_of_creation')
    categories = set(posts.values_list('post_category__category_name', flat=True))
    subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string('notifications/weekly_post.html', {'link': settings.SITE_URL, 'posts': posts})
    msg = EmailMultiAlternatives(subject="Публикации за неделю:", body='', from_email=settings.DEFAULT_FROM_EMAIL,
                                 to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def new_post_notification(preview, pk, post_name, subscribers):
    html_content = render_to_string(
    'notifications/new_post_notification.html',
    {
    'text': preview,
    'link': f'{settings.SITE_URL}/news/{pk}'}
    )

    msg = EmailMultiAlternatives(subject=post_name, body='', from_email=settings.DEFAULT_FROM_EMAIL, to=subscribers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()