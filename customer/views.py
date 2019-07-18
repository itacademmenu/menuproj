from django.shortcuts import render
from .models import UserOrder
from django.views import generic


# Create your views here.
class OrderDetailView(generic.DetailView):
    model = UserOrder
    template_name = 'customer/order_detail.html'


class OrderCreateView(generic.CreateView):
    model = UserOrder
    fields = ['order', 'name', 'sum_paid', 'comment']
    template_name = 'customer/order_create.html'
