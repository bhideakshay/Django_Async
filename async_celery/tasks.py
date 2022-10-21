from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_async_email():
    subject = 'Welcome to django async world'
    message = f'Hi User, This is django async tasks demo.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yourmail@yourdomain.com', ]
    send_mail( subject, message, email_from, recipient_list )