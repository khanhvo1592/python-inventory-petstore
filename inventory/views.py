from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from django.contrib import messages

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'inventory/product_form.html'
    fields = ['sku', 'name', 'quantity', 'aisle', 'bay']
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Product added successfully!')
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'inventory/product_form.html'
    fields = ['sku', 'name', 'quantity', 'aisle', 'bay']
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully!')
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted successfully!')
        return super().delete(request, *args, **kwargs)

def low_stock_view(request):
    low_stock_products = Product.objects.filter(quantity__lt=10)
    return render(request, 'inventory/product_list.html', {'products': low_stock_products})
