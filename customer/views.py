from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .forms import UserOrderForm
from .models import UserOrder
from .utils import time_checker, get_email
from Mproj import settings


class OrderFormView(LoginRequiredMixin, generic.FormView):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), username=request.user.username)
        form = UserOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order.save()
            send_mail('Заказ', 'Вы получили заказ.', settings.EMAIL_HOST_USER, [get_email(request)])
            return redirect('order_detail', slug=order.slug)

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:

            if time_checker(1, 23):

                form = UserOrderForm()
                return render(request, 'customer/order_create.html', {'form': form})
            else:
                return render(request, 'customer/sorry.html')
        else:
            return render(request, 'authentication/permission_denied.html', {'user': 'User'})


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = UserOrder
    template_name = 'customer/order_detail.html'




