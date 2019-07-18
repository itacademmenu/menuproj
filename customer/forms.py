from django import forms
from .models import UserOrder


class UserOrderForm(forms.Form):
    class Meta:
        model = UserOrder

