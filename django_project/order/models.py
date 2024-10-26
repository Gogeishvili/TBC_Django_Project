from django.db import models
from user.models import User
from store.models import Product
from order.managers import UserCartManager


class UserCart(models.Model):
    name = models.CharField(max_length=30, default="user cart")
    user = models.OneToOneField(User, verbose_name="user_cart", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="user_cart", blank=True)


    objects = UserCartManager()

    def __str__(self):
        return f"{self.user.name}'s {self.name}"
    def product_count(self):
        return self.products.count()
