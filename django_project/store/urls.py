from django.urls import path
from store import views


urlpatterns = [
    path("product/", views.product, name="product"),
    path("category/", views.category, name="categories"),
    path("category/product/", views.product_of_category, name="products_of_category"),
]


