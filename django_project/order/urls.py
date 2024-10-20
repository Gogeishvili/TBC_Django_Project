from django.contrib import admin
from django.urls import path
from order import views



urlpatterns = [
    path("", views.order_main_page, name="order_main_page"),
]
