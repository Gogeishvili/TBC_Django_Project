from django.contrib import admin
from store.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_products")
    list_per_page = 2
    search_fields = ("name",)

    @admin.display(description="Products")
    def get_products(self, obj):
        products = obj.products.all()
        return ", ".join([product.name for product in products])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "quantity",
        "get_categories",
        "is_active",
        "get_total_price",
    )
    list_filter = ("category", "is_active")
    search_fields = ("name", "category__name")
    list_select_related = ()
    list_editable = ("price", "quantity", "is_active")
    list_per_page = 5
    autocomplete_fields = ("category",)
    filter_horizontal = ("category",)

    actions=['set_quantity_zero']


    @admin.display(description="Categories")
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    @admin.display(description="ჯამური ფასი")
    def get_total_price(self, obj):
        return obj.price * obj.quantity

    @admin.action(description="set quantity Zero")
    def set_quantity_zero(self, request, queryset):
        queryset.update(quantity=0)
