from django.conf import settings
from django import forms
from django.core.exceptions import ValidationError
from store.models import Product
from django.utils.text import slugify


# class ProductFormTest(forms.Form):
#     name = forms.CharField(max_length=30)
#     price = forms.FloatField()
#     quantity = forms.IntegerField()
#     image = forms.ImageField()

#     def clean_price(self):
#         price=self.cleaned_data['price']
#         if price<0:
#             raise ValidationError('Price must be positiove')
        

class ProductFormTest(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude=['is_active','slug']  

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Price must be positive.')
        return price


    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise ValidationError('Quantity must be positive.')
        return quantity

    def clean_slug(self):
        name = self.cleaned_data.get('name')
        if name:
            slug = slugify(name)
            if Product.objects.filter(slug=slug).exists():
                raise ValidationError('This slug is already in use. Please choose another name.')
            return slug
        raise ValidationError('This field is required.')



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