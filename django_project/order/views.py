from django.db.models import *
from django.shortcuts import render, get_object_or_404, redirect
from order.models import UserCart
from store.models import Product
from .models import UserCart,CartItem
from .forms import UserCartForm
from django.views.generic import *


def chackout(request):
    return render(request,'chackout.html',{})

class UserCartView(ListView):
    model = CartItem
    template_name = 'cart.html'  

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.get_queryset()
        total_price = sum(item.get_total_price() for item in cart_items)
        context['total_price'] = total_price
        return context


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))  
        product = get_object_or_404(Product, id=product_id)

        if quantity > product.quantity:
            return redirect('store:category')  
        
        user_cart, created = UserCart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        if not created: 
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        
        cart_item.save()  #

        
        product.quantity -= quantity
        product.save()
        
        return redirect('order:cart')  

class UpdateCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        user_cart = get_object_or_404(UserCart, user=request.user)

        cart_item = get_object_or_404(CartItem, cart=user_cart, product_id=product_id)

        if quantity <= 0:
            cart_item.delete()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return redirect('order:cart')

class DeleteFromCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        user_cart = get_object_or_404(UserCart, user=request.user)

        try:
            cart_item = CartItem.objects.get(cart=user_cart, product_id=product_id)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass  

        return redirect('order:cart')