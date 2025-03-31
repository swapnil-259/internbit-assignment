from django.contrib.auth.models import User
from django.db import models

from apps.core.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=None)


class Transaction(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="transaction_user"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name="transaction_product",
    )
    quantity = models.BigIntegerField(default=1)
    amount = models.FloatField(default=None)
