from django.urls import path
from order import views

app_name='order'

urlpatterns = [
    path("cart/", views.order_main_page, name="order_main_page"),
]
