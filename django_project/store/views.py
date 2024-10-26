from django.shortcuts import render
from store.models import Product, Category
from django.db.models import *
from django.shortcuts import render
from .models import Product,ProductTags
from django.views.generic import ListView



def index(request):
    return render(request, "index.html", {})


def contact(request):
    return render(request, "contact.html", {})


#Category Class view
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