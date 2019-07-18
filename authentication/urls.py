from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.RedirectView.as_view(), name='index'),
    path('register/', views.register, name='register'),
]
