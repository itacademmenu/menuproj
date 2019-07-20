from django import forms

from .models import UserOrder


class UserOrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = ('order', 'name', 'sum_paid', 'comment')