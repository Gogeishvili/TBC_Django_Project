from django.db.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from order.models import UserCart
from django.shortcuts import get_object_or_404, redirect
from store.models import Product
from .models import UserCart
from .forms import UserCartForm
from django.views.generic import *



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

class UserCartView(ListView):
    model = UserCart
    template_name = "cart.html"
    context_object_name = "user_cart"

    def get_queryset(self):
        user_cart, created = UserCart.objects.get_or_create(user=self.request.user)
        return user_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cart = self.get_queryset()
    
        context['products'] = [
            {
                'product': Product.objects.get_product_by_id(product_id),  # Use the new method
                'quantity': quantity,
                'total_price': Product.objects.get_product_by_id(product_id)['sum_price'] * quantity,
            }
            for product_id, quantity in user_cart.quantities.items() if Product.objects.get_product_by_id(product_id)
        ]
        
        return context

