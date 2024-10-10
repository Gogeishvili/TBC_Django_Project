from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category


def index(request):
    return HttpResponse("THIS IS STORE MAIN PAGE")


def products(request):
    products = Product.objects.all()
    products_list = []

    for product in products:
        categories_data = [
            {"id": category.id, "name": category.name} 
            for category in product.category.all()
        ]

        if categories_data:
            products_list.append({
                "id": product.id,
                "name": product.name,
                "image_URL":request.build_absolute_uri(product.image.url) if product.image else None,
                "categories": categories_data  
            })

    return JsonResponse(products_list,safe=False)


def categories(request):
    categories = Category.objects.all()
    categories_list = []
    for category in categories:
        if category.parent:
            parent_data = {"id": category.parent.id, "name": category.parent.name}
        else:
            parent_data = None

        categories_list.append(
            {"id": category.id, "name": category.name, "parent": parent_data}
        )

    return JsonResponse(categories_list,safe=False)
