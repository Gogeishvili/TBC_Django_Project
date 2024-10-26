from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from store.forms import ProductFormTest,ProductForm
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from order.models import UserCart
from django.core.paginator import Paginator



def test(request):
    name = None
    price = None
    quantity = None
    image_url = None

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        image = request.FILES.get("image")

        if image:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT / "product")
            filename = fs.save(image.name, image)
            image_url = fs.url(f"product/{filename}")

    return render(
        request,
        "store/test.html",
        {"name": name, "price": price, "quantity": quantity, "image_url": image_url},
    )


def form_test(request):
    products = Product.objects.all()

    search_query = request.GET.get('name', '')
    if search_query:
        products = products.filter(name__icontains=search_query)  

    if request.method == "POST":
        form = ProductFormTest(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False) 
            new_product.slug = slugify(new_product.name) 
            new_product.save()
            return render(request, "store/test_form.html", {"products": products, "form": ProductFormTest(), 'search': search_query})

    else:
        form = ProductFormTest()  

    return render(request, "store/test_form.html", {
        "products": products, 
        "form": form,
        'search': search_query  
    })


def index(request):
    return render(request, "index.html", {})


def category(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(products__is_active=True).distinct()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(name__icontains=search_query)

    # Category filter
    selected_category = request.GET.get('category')
    if selected_category:
        products = products.filter(category__id=selected_category)

    # Pagination
    paginator = Paginator(products, 6)  # Show 6 products per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    products = paginator.get_page(page_number)  # Get the products for the current page

    return render(request, "shop.html", {
        "products": products,
        "categories": categories,
        "search_query": search_query,
        "selected_category": selected_category,
        "paginator": paginator,  # Pass paginator to the template
    })


def product(request):
    pass


def contact(request):
    return render(request, "contact.html", {})
