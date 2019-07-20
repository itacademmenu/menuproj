from django.conf import settings
from django.core.mail import send_mail
from customer.models import UserOrder


def email(recipient, *args, delete=False):
    recipient_list = []
    recipient_list.append(recipient)
    if delete:
        message = 'Приносим извинения, ваш заказ {0} был удален.\nПричина:{1}'.format(*args)
    else:
        message = 'Детали вашего заказа были изменены на:\nЗаказ: {0}\nКомментарий: {1}'.format(*args)
    subject = 'Заказ у menuservice'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)


def get_email(request):
    obj = UserOrder.objects.get(pk=request.data['id'])
    mail = obj.user.email
    return mail


def get_message(request):
    obj = UserOrder.objects.get(pk=request.data['id'])
    order = obj.order
    comment = obj.comment
    message = [order, comment]
    return message