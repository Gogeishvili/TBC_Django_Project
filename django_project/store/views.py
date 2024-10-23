from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *




def test_2(request):
    return render(request, "test2.html", {})

def index(request):
    return render(request, "index.html", {})


def category(request):
    categories_without_parent = Category.objects.filter(parent__isnull=True)
    return render(
        request,
        "shop.html",
        {"categories_without_parent": categories_without_parent},
    )


def product(request):
    products = Product.objects.get_all_active_products()
    return render(request, "shop-detail.html", {"products": products})


def contact(request):
    return render(request, "contact.html", {})
