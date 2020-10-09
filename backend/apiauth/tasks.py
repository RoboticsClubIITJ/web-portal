from config.celery import app as celery_app # noqa: ignore=F401 
from celery import shared_task

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_welcome_email(name, email):
    subject = 'Welcome to Robotics club IITJ'
    message = f'Hi {name}, thank you for registering with Robotics Club'
    email_from = EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)
