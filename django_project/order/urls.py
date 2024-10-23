from django.urls import path
from order import views

app_name='order'

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("chackout/", views.chackout, name="chackout"),
]
