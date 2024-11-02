from django.urls import path
from . import views


app_name='store'

urlpatterns = [
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("", views.IndexView.as_view(), name="index"),
]



