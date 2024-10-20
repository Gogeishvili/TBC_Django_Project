from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *


def test_HTML(request):
    products = Product.objects.prefetch_related("category").all()
    categories = Category.objects.prefetch_related("products").all().annotate(products_count=Count('products'))
    return render(
        request, "test.html", {
            "products": products,
            "categories": categories}
    )


def product_JSON(request):
    products = Product.objects.get_products_JSON()
    return JsonResponse(products, safe=False)


def category_JSON(request):
    categories = Category.objects.get_category_JSON()
    return JsonResponse(categories, safe=False)


def product(request):
    products = Product.objects.get_all_active_products()
    return render(request, "product.html", {"products": products})


def product_of_category(request):
    category_summary = Category.objects.get_category_summary()
    most_expensive = Category.objects.get_most_expensive_product()
    cheapest = Category.objects.get_cheapest_product()
    average_price = Category.objects.get_average_product_price()

    return render(
        request,
        "productsOfCategory.html",
        {
            "category_summary": category_summary,
            "most_expensive": most_expensive,
            "cheapest": cheapest,
            "average_price": average_price,
        },
    )


def category(request):
    categories_without_parent = Category.objects.filter(parent__isnull=True)
    return render(
        request,
        "category.html",
        {"categories_without_parent": categories_without_parent},
    )
