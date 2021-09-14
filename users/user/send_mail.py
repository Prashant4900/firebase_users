from django.conf import settings
from django.core.mail import send_mail


def send_custom_email(email, link):
    subject = 'welcome to GFG world'
    message = f'Hi {email}, thank you for registering in geeksforgeeks. {link}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)
