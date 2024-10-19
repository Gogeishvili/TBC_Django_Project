from django.urls import path
from store import views


urlpatterns = [
    path('product/JSON/',views.product_JSON,name='product_JSON'),
    path('category/JSON/',views.category_JSON,name='category_JSON'),
    path("product/", views.product, name="product"),
    path("category/", views.category, name="category"),
    path("category/product/", views.product_of_category, name="products_of_category"),
]


