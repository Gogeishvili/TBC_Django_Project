from django.db import models


class ProductManager(models.Manager):

    def get_active_products(self):
        return self.get_queryset().filter(is_active=True)