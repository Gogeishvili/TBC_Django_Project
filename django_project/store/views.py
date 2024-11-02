from django.shortcuts import render
from django.db.models import *
from django.shortcuts import render
from django.views.generic import *
from .models import Product, ProductTags, Category
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class ProductView(DetailView):
    template_name='product.html'
    model=Product
    context_object_name='product'

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs['product_id'])


@method_decorator(login_required(login_url="user:login"), name="dispatch")
class CategoryView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        search_query = self.request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        selected_category = self.request.GET.get("category")
        if selected_category:
            queryset = queryset.filter(category__id=selected_category)

        selected_tag = self.request.GET.get("tag")
        if selected_tag:
            queryset = queryset.filter(tag__name=selected_tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter( products__is_active=True).distinct()
        context["all_tags"] = ProductTags.objects.all()
        context["search_query"] = self.request.GET.get("search", "")
        context["selected_category"] = self.request.GET.get("category")
        context["selected_tag"] = self.request.GET.get("tag")


        return context
