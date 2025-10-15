from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products"
    paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/details.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    template_name = "products/create.html"
    fields = ["name","description","price","stock"]
    success_url = reverse_lazy("product-list")

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/update.html"
    fields = ["name","description","price","stock"]
    success_url = reverse_lazy("product-list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("product-list")