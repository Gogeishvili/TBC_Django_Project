from django.urls import path
from order import views

app_name='order'

urlpatterns = [
    path("cart/", views.UserCartView.as_view(), name="cart"),
    path("chackout/", views.chackout, name="chackout"),
    path("add_to_cart/<int:product_id>/", views.AddToCartView.as_view(), name="add_to_cart"),
    path('delete-from-cart/<int:product_id>/', views.DeleteFromCartView.as_view(), name='delete_from_cart'),
]
