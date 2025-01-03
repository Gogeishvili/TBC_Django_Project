"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from .import views
from django.conf.urls.i18n import i18n_patterns,set_language

urlpatterns = i18n_patterns(
    path('set_language/',set_language, name='set_language'),
    path("admin/", admin.site.urls,name='admin'),
    path("user/", include("user.urls", namespace="user")),
    path("order/", include("order.urls", namespace="order")),
    path("404/", views.custom_404_view, name="404"),
    path("500/", views.custom_500_view, name="500"),
    path("", include("store.urls", namespace="store")),
    prefix_default_language=False
) + debug_toolbar_urls()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


