from django.db import models
from user.models import User
from store.models import Product
from order.managers import UserCartManager


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="user_cart", blank=True)
    quantities = models.JSONField(default=dict)

    def add_product(self, product, quantity):
        if product.id in self.quantities:
            self.quantities[product.id] += quantity
        else:
            self.quantities[product.id] = quantity
        self.save()

    def get_total_price(self):
        total_price = 0
        for product_id, quantity in self.quantities.items():
            product = Product.objects.get(id=product_id)
            total_price += product.price * quantity
        return total_price

    def product_count(self):
        return sum(self.quantities.values())

    def clear_cart(self):
        self.quantities.clear()
        self.save()
