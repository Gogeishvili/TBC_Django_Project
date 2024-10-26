from django import forms
from .models import UserCart
from store.models import Product

class UserCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1)

    def clean(self):
        cleaned_data = super().clean()
        product_id = cleaned_data.get('product_id')
        quantity = cleaned_data.get('quantity')
        
        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise forms.ValidationError("The product does not exist.")
        if quantity > product.quantity:
            raise forms.ValidationError("Not enough stock available for this product.")
        
        return cleaned_data