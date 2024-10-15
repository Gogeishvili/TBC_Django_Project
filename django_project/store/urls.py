from django.urls import path
from store import views


urlpatterns = [
    path("index/", views.index, name="index"),
    path("product/info/", views.products, name="products"),
    path("category/info/", views.categories, name="categories"),
]


