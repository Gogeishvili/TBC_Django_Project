from django.urls import path
from store import views

app_name='store'

urlpatterns = [
    path("", views.index, name="index"),
    path("category/", views.category, name="category"),
    path("product/", views.product, name="product"),
    path("contact/",views.contact,name="contact"),
    path('test/',views.test_2,name='test_2'),
]



