from django.db import models
from django.shortcuts import get_object_or_404
from store.models import Product

class UserCartManager(models.Manager):
    def get_or_create_cart(self, user):
        return self.get_or_create(user=user)

    def add_product(self, user, product, quantity):
        user_cart, created = self.get_or_create(user=user)
        
        if str(product.id) in user_cart.quantities:
            user_cart.quantities[str(product.id)]['quantity'] += quantity
        else:
            user_cart.quantities[str(product.id)] = {
                'name': product.name,
                'price': float(product.price),
                'quantity': quantity,
                'image_url': product.image.url if product.image else None,
            }
        user_cart.save()
        return user_cart
    
    def add_product(self, product, quantity):
        if str(product.id) in self.quantities:
            self.quantities[str(product.id)] += quantity
        else:
            self.quantities[str(product.id)] = quantity
        self.save()

    def get_total_price(self):
        total_price = 0
        for product_id, quantity in self.quantities.items():
            try:
                product = Product.objects.get(id=product_id)
                total_price += product.price * quantity
            except Product.DoesNotExist:
                continue
        return total_price

    def product_count(self):
        return sum(self.quantities.values())

    def clear_cart(self):
        self.quantities.clear()
        self.products.clear()
        self.save()