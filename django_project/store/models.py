from math import trunc
from django.db import models
from store.Managers import ProductManager, CategoryManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

    objects = CategoryManager()


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category, related_name="products")
    image = models.ImageField(upload_to="product/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    objects = ProductManager()
