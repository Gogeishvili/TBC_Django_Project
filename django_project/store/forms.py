from django.conf import settings
from django import forms
from django.core.exceptions import ValidationError
from store.models import Product
from django.utils.text import slugify    





class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude=['is_active','slug']  
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise ValidationError('Quantity must be positive.')
        return quantity