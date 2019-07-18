from django import forms
from .models import UserOrder


class UserOrderForm(forms.ModelForm):
    disabled_fields = ('order', 'name', 'sum_paid', 'comment',)


    class Meta:
        model = UserOrder
        fields = '__all__'


