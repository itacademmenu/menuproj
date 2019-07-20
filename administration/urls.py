from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.AdminView.as_view(), name='administration'),
    path('orders/', views.OrderViewList.as_view(), name='orders'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('orders/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('orders/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
]