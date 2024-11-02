from django.urls import path
from . import views
from django.views.generic import ListView


app_name='store'

urlpatterns = [
    path("contact/",views.contact,name="contact"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("", views.index, name="index"),
]



