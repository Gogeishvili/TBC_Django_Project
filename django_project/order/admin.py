from django.contrib import admin
from order.models import UserCart

@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "product_count_display",
        "get_products", 
        "get_total_price",
    )
    list_filter = ("name",)
    search_fields = ("user__username", "name")
    list_per_page = 10

    actions = ['clear_cart']

    @admin.display(description="Product Count")
    def product_count_display(self, obj):
        return obj.product_count()
    
    @admin.display(description="Products (Name and ID)")
    def get_products(self, obj):
        return ", ".join([f"{product.name} (ID: {product.id})" for product in obj.products.all()])

    @admin.display(description="Total Price")
    def get_total_price(self, obj):
        total_price = sum(product.price for product in obj.products.all())
        return total_price

    @admin.action(description="Clear Cart")
    def clear_cart(self, request, queryset):
        for cart in queryset:
            cart.products.clear()  

