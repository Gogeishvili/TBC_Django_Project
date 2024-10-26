from django.contrib import admin
from order.models import UserCart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    fields = ("product", "quantity", "get_product_price", "get_total_price")
    readonly_fields = ("get_product_price", "get_total_price")

    def get_product_price(self, obj):
        return obj.product.price if obj.product else "N/A"

    get_product_price.short_description = "Product Price"

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity if obj.product else "N/A"

    get_total_price.short_description = "Total Price"


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ("user", "get_total_cart_price", "product_count")

    def get_total_cart_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())

    get_total_cart_price.short_description = "Total Cart Price"

    def product_count(self, obj):
        return sum(item.quantity for item in obj.items.all())

    product_count.short_description = "Total Products"
