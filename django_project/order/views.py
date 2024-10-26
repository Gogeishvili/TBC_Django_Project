from django.db.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from order.models import UserCart
from django.shortcuts import get_object_or_404, redirect
from store.models import Product
from .models import UserCart
from .forms import UserCartForm


def test(request):
    return render(request,'order/test.html')

def cart(request):
    return render(request,'cart.html',{})

def chackout(request):
    return render(request,'chackout.html',{})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = UserCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if quantity > product.quantity:
                form.add_error('quantity', "Not enough stock available for this product.")
                return render(request, 'store/shop_test.html', {
                    'form': form,
                    'products': Product.objects.all()
                })
            user_cart, created = UserCart.objects.get_or_create(user=request.user)
            user_cart.add_product(product, quantity)
            product.quantity -= quantity
            product.save()
            return redirect('store:category')

    else:
        form = UserCartForm()

    return render(request, 'store/shop_test.html', {
        'products': Product.objects.all()
    })

