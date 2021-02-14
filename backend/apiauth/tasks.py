from config.celery import app as celery_app # noqa: ignore=F401 
from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from config.settings import EMAIL_HOST_USER


@shared_task
def send_welcome_email(name, email):
    subject = 'Welcome to Robotics club IITJ'
    html_content = render_to_string("email.html", {'user': name})
    text_content = strip_tags(html_content)
    message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=EMAIL_HOST_USER, to=[email, ])
    message.attach_alternative(html_content, "text/html")
    message.send()


@shared_task
def send_thinkathon_email(name, team, email):
    subject = 'Thinkathon 2021 Team Registration'
    html_content = render_to_string("thinkathonemail.html", {'user': name, 'team': team})
    text_content = strip_tags(html_content)
    message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=EMAIL_HOST_USER, to=[email, ])
    message.attach_alternative(html_content, "text/html")
    message.send()
