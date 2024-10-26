from django.urls import path
from store import views
from django.views.generic import ListView


app_name='store'

urlpatterns = [
    path('test/',views.test,name='store_test'),
    path('test_form/',views.form_test,name='store_test_form'),
    path("category/", views.CategoryView.as_view(), name="category"),


    path("product/", views.product, name="product"),
    path("contact/",views.contact,name="contact"),
    path("", views.index, name="index"),
]



