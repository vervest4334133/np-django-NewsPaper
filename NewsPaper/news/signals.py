
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post, PostCategory

from django.conf import settings


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
    'notifications/new_post_notification.html',
    {
    'text': preview,
    'link': f'{settings.SITE_URL}/news/{pk}'}
    )

    msg = EmailMultiAlternatives(subject=title, body='', from_email=settings.DEFAULT_FROM_EMAIL, to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def new_post_released(sender, instance: list[str], **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.post_category.all()
        subscribers = []

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)

