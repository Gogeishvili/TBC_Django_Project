from django.urls import path
from store import views

app_name='store'

urlpatterns = [
    path('testHTML/',views.test_HTML,name='test_HTML'),
    path('product/JSON/',views.product_JSON,name='product_JSON'),
    path('category/JSON/',views.category_JSON,name='category_JSON'),
    path("category/product/", views.product_of_category, name="products_of_category"),

    #new urls
    path("", views.index, name="index"),
    path("category/", views.category, name="category"),
    path("product/", views.product, name="product"),
]



