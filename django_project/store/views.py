from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *


def product(request):
    categories = Category.objects.prefetch_related("products")
    products = (
        Product.objects.prefetch_related("category")
        .annotate(total=F("quantity") * F("price"))
        .aggregate(sub_total=Sum("total"))
    )

    return render(
        request, "product.html", {"categories": categories, "products": products}
    )


def product_of_category(request):
    return render(request, "productsOfCategory.html", {})


def category(request):
    categories_without_parent = Category.objects.filter(parent__isnull=True)
    return render(
        request,
        "category.html",
        {"categories_without_parent": categories_without_parent},
    )
