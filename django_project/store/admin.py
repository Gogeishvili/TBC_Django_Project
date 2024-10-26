from django.contrib import admin
from store.models import Category, Product,ProductTags


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_category", "get_products")  
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)} 

    @admin.display(description="Parent Category")
    def parent_category(self, obj):
        return obj.parent.name if obj.parent else "None"

    @admin.display(description="Products")
    def get_products(self, obj):
        products = obj.products.all()
        return ", ".join([product.name for product in products])


@admin.register(ProductTags)
class ProductTagsAdmin(admin.ModelAdmin):
    list_display = ("name", "get_products")
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
        "get_product_tag",
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
    prepopulated_fields = {"slug": ("name",)} 

    actions=['set_quantity_zero']


    @admin.display(description="Categories")
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    
    @admin.display(description="Tags")
    def get_product_tag(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    @admin.display(description="Total Price")
    def get_total_price(self, obj):
        return obj.price * obj.quantity

    @admin.action(description="set quantity Zero")
    def set_quantity_zero(self, request, queryset):
        queryset.update(quantity=0)
