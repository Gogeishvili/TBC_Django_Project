from math import trunc
from django.db import models
from django_project.store.managers import ProductManager, CategoryManager
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CategoryManager()

    def __str__(self):
        return f"{self.name}"


class ProductTags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category, related_name="products")
    tag = models.ManyToManyField(ProductTags, related_name="products")
    image = models.ImageField(upload_to="product/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()



    def __str__(self):
        return f"{self.name}"
