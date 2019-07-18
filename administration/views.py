from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings


class AdminView(generic.TemplateView):
    template_name = 'administration/administration.html'


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['garick@bk.ru', 'afdaf@afa.ru']
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)



