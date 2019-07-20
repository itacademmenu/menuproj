from rest_framework import serializers, generics
from rest_framework.permissions import IsAdminUser
from django.views import generic

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from customer.models import UserOrder
from .utils import email, get_email, get_message


class AdminView(LoginRequiredMixin, generic.View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'administration/administration.html')
        else:
            return render(request, 'authentication/permission_denied.html', {'user': 'Admin'})


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserOrder
        fields = ['id', 'name', 'order', 'comment', 'sum_paid']

        def update(self, request):
            print(request.data)


class OrderViewList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserOrder.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserOrder.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.data['id'])
        self.check_object_permissions(self.request, obj)
        return obj
>>>>>>> 717ff47571095822d299fd2cbe9546cc4302164e

    def update(self, request, *args, **kwargs):
        response = super(OrderUpdateView, self).update(request)
        mail = get_email(request)
        message = get_message(request)
        email(mail, *message)
        return response


class OrderDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserOrder.objects.all()
    serializer_class = OrderSerializer

<<<<<<< HEAD
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['garick@bk.ru', 'afdaf@afa.ru']
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

=======
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.data['id'])
        print(obj)
        self.check_object_permissions(self.request, obj)
        return obj
>>>>>>> 717ff47571095822d299fd2cbe9546cc4302164e

    def destroy(self, request, *args, **kwargs):
        mail = get_email(request)
        message = get_message(request)
        email(mail, *message, delete=True)
        response = super(OrderDeleteView, self).destroy(request)
        return response

