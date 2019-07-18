from django.shortcuts import render, get_object_or_404
from datetime import datetime

from django.urls import reverse_lazy

from .models import UserOrder
from django.views.generic import DetailView, CreateView
from .forms import UserOrderForm


class OrderDetailView(DetailView):
    model = UserOrder
    fields = '__all__'
    template_name = 'customer/order_detail.html'


def valid_time(request):
    return render(request, 'customer/sorry.html')


class OrderCreateView(CreateView):

#if '13:00:00' < datetime.now().strftime('%H:%M:%S') < '15:00:00':
    model = UserOrder
    fields = ['order', 'name', 'sum_paid', 'comment']
    template_name = 'customer/order_create.html'
    success_url = reverse_lazy('order_detail')



    # else:
    #     model = UserOrder
    #     fields = ['order', 'name', 'sum_paid', 'comment']
    #     template_name = 'customer/sorry.html'




