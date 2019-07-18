from django.urls import path
from .views import *


urlpatterns = [
    path('detail/<slug:slug>', OrderDetailView.as_view(), name='order_detail'),
    path('', OrderCreateView.as_view(), name='order_create')
]