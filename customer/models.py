import uuid

from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class UserOrder(models.Model):
    order = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    sum_paid = models.CharField(max_length=10, validators=[validate_comma_separated_integer_list])
    comment = models.TextField(max_length=200, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders',)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.order

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={"slug": self.slug})
