from django.contrib import admin
from django.urls import path
from store import views


urlpatterns = [
    path("", views.index, name="index"),
    path("product/info/", views.products, name="products"),
    path("category/info/", views.categories, name="categories"),
]
