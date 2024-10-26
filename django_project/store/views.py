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
from .models import Product,ProductTags
from django.contrib.auth.decorators import login_required
from order.models import UserCart
from django.core.paginator import Paginator
from django.views.generic import ListView




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
    all_tags = ProductTags.objects.all() 

   
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(name__icontains=search_query)

    
    selected_category = request.GET.get('category')
    if selected_category:
        products = products.filter(category__id=selected_category)

    
    selected_tag = request.GET.get('tag')  
    if selected_tag:
        products = products.filter(tag__name=selected_tag)  

    
    paginator = Paginator(products, 6) 
    page_number = request.GET.get('page')  
    products = paginator.get_page(page_number)  

    return render(request, "shop.html", {
        "products": products,
        "categories": categories,
        "search_query": search_query,
        "selected_category": selected_category,
        "selected_tag": selected_tag,  
        "all_tags": all_tags,  
        "paginator": paginator,  
    })

class CategoryView(ListView):
    model = Product
    template_name = "shop.html"  
    context_object_name = "products"
    paginate_by = 6 

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        selected_category = self.request.GET.get('category')
        if selected_category:
            queryset = queryset.filter(category__id=selected_category)

        selected_tag = self.request.GET.get('tag')
        if selected_tag:
            queryset = queryset.filter(tag__name=selected_tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(products__is_active=True).distinct()
        context['all_tags'] = ProductTags.objects.all()
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category')
        context['selected_tag'] = self.request.GET.get('tag')

        return context

def product(request):
    pass


def contact(request):
    return render(request, "contact.html", {})
