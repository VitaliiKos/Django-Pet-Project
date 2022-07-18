from django.contrib.auth.models import User
from django.db import models

from apps.products.models import ProductModel
from apps.user.models import UserModel

# class UserModel(models.Model):
#     name = models.CharField(max_length=255, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "{} - {} - {}".format(self.name,
#                                      self.created_at,
#                                      self.updated_at)


class Cart(models.Model):
    class Meta:
        db_table = 'cart'

    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.user,
            self.item,
            self.quantity,
            self.created_at,
            self.updated_at)
