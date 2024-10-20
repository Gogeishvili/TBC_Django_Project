from django.urls import path
from store import views


urlpatterns = [
    path('testJSON/',views.test_JSON,name='test_JSON'),
    path('testHTML/',views.test_HTML,name='test_HTML'),
    path('product/JSON/',views.product_JSON,name='product_JSON'),
    path('category/JSON/',views.category_JSON,name='category_JSON'),
    path("product/", views.product, name="product"),
    path("category/", views.category, name="category"),
    path("category/product/", views.product_of_category, name="products_of_category"),
]



