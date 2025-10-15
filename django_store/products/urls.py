from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('',ProductListView.as_view(),name='product-list'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('add/',ProductCreateView.as_view(),name='product-add'),
    path('edit/<int:pk>',ProductUpdateView.as_view(),name='product-edit'),
    path('delete/<int:pk>',ProductDeleteView.as_view(),name='product-delete'),
]