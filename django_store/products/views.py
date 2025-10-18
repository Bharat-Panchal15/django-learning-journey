from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product
from .mixins import StaffRequiredMixin

# Create your views here.

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/details.html"
    context_object_name = "product"

class ProductCreateView(LoginRequiredMixin,StaffRequiredMixin, CreateView):
    model = Product
    template_name = "products/create.html"
    fields = ["name","description","price","stock"]
    success_url = reverse_lazy("product-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "products/update.html"
    fields = ["name","description","price","stock"]
    success_url = reverse_lazy("product-list")

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "products/delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("product-list")