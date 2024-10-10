from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category


def index(request):
    return HttpResponse("THIS IS STORE MAIN PAGE")


def products(request):
    products = Product.objects.all().values()
    return JsonResponse({"Products": list(products)})


def categories(request):
    categories = Category.objects.all().values()
    return JsonResponse({"Categories": list(categories)})
