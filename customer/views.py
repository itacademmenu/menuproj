from django.shortcuts import render
from .models import UserOrder
from django.views.generic import DetailView, CreateView


class OrderDetailView(DetailView):
    model = UserOrder
    template_name = 'customer/order_detail.html'


class OrderCreateView(CreateView):
    model = UserOrder
    fields = ['order', 'name', 'sum_paid', 'comment']
    template_name = 'customer/order_create.html'

