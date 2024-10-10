from django.urls import path
from django_project import settings
from store import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("product/info/", views.products, name="products"),
    path("category/info/", views.categories, name="categories"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
