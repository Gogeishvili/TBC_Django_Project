from django.db import models
from django.shortcuts import get_object_or_404
from store.models import Product

class UserCartManager(models.Manager):
    def get_or_create_cart(self, user):
        return self.get_or_create(user=user)

    def add_product(self, user, product_id, quantity):
        
        if not user.is_authenticated:
            return False, "You need to log in to add products to the cart."

        product = get_object_or_404(Product, id=product_id)
        user_cart, _ = self.get_or_create(user=user)

        if quantity < 1:
            return False, "Quantity must be at least 1."

        if quantity > product.quantity:
            return False, f"Only {product.quantity} unit(s) available."

        if product not in user_cart.products.all():
            user_cart.products.add(product)
            message = f"{quantity} unit(s) of {product.name} added to your cart."
        else:
            message = "Product is already in your cart."

        product.quantity -= quantity
        product.save()

        return True, message