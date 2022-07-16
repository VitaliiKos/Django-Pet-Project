from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from apps.products.models import ProductModel
# from shop.models.cart import CartItemManager


class CartModel(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('CartModel', on_delete=models.CASCADE)

    def price_ttc(self):
        return self.price_ht

    def __str__(self):
        return self.product
