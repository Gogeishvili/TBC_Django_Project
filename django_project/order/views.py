from django.shortcuts import render
from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from store.forms import ProductFormTest,ProductForm
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from order.models import UserCart
from django.contrib import messages
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
                return render(request, 'store/sho_text.html', {
                    'form': form,
                    'products': Product.objects.all()
                })

           
            user_cart, created = UserCart.objects.get_or_create(user=request.user)
            cart_item, created = user_cart.products.through.objects.get_or_create(
                usercart=user_cart,
                product=product,
            )        
            cart_item.save()
            return redirect('store:category')  

    else:
        form = UserCartForm()  

    return render(request, 'store/shop_text.html', {
        'products': Product.objects.all()
    })