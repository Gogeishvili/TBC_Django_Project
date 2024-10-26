from django.contrib import admin
from order.models import UserCart

@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product_count_display",
        "get_products", 
        "get_total_price",
    )
    list_filter = ("user",)
    search_fields = ("user__username",)
    list_per_page = 10

    actions = ['clear_cart']

    @admin.display(description="Product Count")
    def product_count_display(self, obj):
        return obj.product_count()
    
    @admin.display(description="Products (Name and ID)")
    def get_products(self, obj):
        products_info = []
        for product in obj.products.all():
            quantity = obj.quantities.get(str(product.id), 0) 
            products_info.append(f"{product.name} (ID: {product.id}, Quantity: {quantity})")
        return ", ".join(products_info)

    @admin.display(description="Total Price")
    def get_total_price(self, obj):
        return obj.get_total_price()

    @admin.action(description="Clear Cart")
    def clear_cart(self, request, queryset):
        for cart in queryset:
            cart.clear_cart() 

