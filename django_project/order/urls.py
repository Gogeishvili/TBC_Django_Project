from django.urls import path
from order import views

app_name='order'

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("chackout/", views.chackout, name="chackout"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),  
    path("test/",views.test,name="order_test")
]
