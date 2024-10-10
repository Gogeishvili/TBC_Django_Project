from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="product/", blank=False, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}"
