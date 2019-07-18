from django.urls import path
from . import views


urlpatterns = [
    path('detail/<slug:slug>', views.OrderDetailView.as_view(), name='order_detail'),
    path('', views.OrderCreateView.as_view(), name='order')
]

