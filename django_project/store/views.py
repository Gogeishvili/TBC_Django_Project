from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *


def product_test(request):
    products = Product.objects.product_test()
    return JsonResponse(products, safe=False)


def category_test(request):
    catgories = Category.objects.category_test()
    return JsonResponse(catgories, safe=False)


def product_JSON(request):
    products = Product.objects.get_products_JSON()
    return JsonResponse(products, safe=False)


def category_JSON(request):
    categories = Category.objects.get_category_JSON()
    return JsonResponse(categories, safe=False)


def product(request):
    products = Product.objects.all()
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
