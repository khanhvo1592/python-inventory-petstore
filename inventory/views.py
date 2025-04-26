from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Supply, Location
from .forms import LocationForm
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    permission_required = 'inventory.can_view_product'

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'inventory/product_form.html'
    fields = ['sku', 'name', 'quantity', 'location']
    success_url = reverse_lazy('product_list')
    permission_required = 'inventory.can_edit_product'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Product added successfully!')
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'inventory/product_form.html'
    fields = ['sku', 'name', 'quantity', 'location']
    success_url = reverse_lazy('product_list')
    permission_required = 'inventory.can_edit_product'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'inventory.can_edit_product'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted successfully!')
        return super().delete(request, *args, **kwargs)

@login_required
@permission_required('inventory.can_view_product')
def low_stock_view(request):
    low_stock_products = Product.objects.filter(quantity__lt=10)
    return render(request, 'inventory/product_list.html', {'products': low_stock_products})

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return render(request, 'inventory/logout.html')

@login_required
def user_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('product_list')
    
    users = User.objects.all().order_by('username')
    return render(request, 'inventory/user_management.html', {'users': users})

# Location Views
@login_required
@permission_required('inventory.can_edit_supply', raise_exception=True)
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'inventory/location_list.html', {'locations': locations})

@login_required
@permission_required('inventory.can_edit_supply', raise_exception=True)
def location_create(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        if Location.objects.filter(code=code).exists():
            messages.error(request, 'Location code already exists.')
            return render(request, 'inventory/location_form.html')
        
        Location.objects.create(code=code, name=name)
        messages.success(request, 'Location created successfully.')
        return redirect('location_list')
    return render(request, 'inventory/location_form.html')

@login_required
@permission_required('inventory.can_edit_supply', raise_exception=True)
def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        
        if code != location.code and Location.objects.filter(code=code).exists():
            messages.error(request, 'Location code already exists.')
            return render(request, 'inventory/location_form.html', {'location': location})
        
        location.code = code
        location.name = name
        location.save()
        messages.success(request, 'Location updated successfully.')
        return redirect('location_list')
    return render(request, 'inventory/location_form.html', {'location': location})

@login_required
@permission_required('inventory.can_edit_supply', raise_exception=True)
def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        messages.success(request, 'Location deleted successfully.')
        return redirect('location_list')
    return render(request, 'inventory/location_confirm_delete.html', {'location': location})

# Supply Views
class SupplyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supply
    template_name = 'inventory/supply_list.html'
    context_object_name = 'supplies'
    permission_required = 'inventory.can_view_supply'

class SupplyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Supply
    template_name = 'inventory/supply_form.html'
    fields = ['name', 'quantity', 'location', 'price']
    success_url = reverse_lazy('supply_list')
    permission_required = 'inventory.can_edit_supply'

class SupplyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supply
    template_name = 'inventory/supply_form.html'
    fields = ['name', 'quantity', 'location', 'price']
    success_url = reverse_lazy('supply_list')
    permission_required = 'inventory.can_edit_supply'

class SupplyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supply
    template_name = 'inventory/supply_confirm_delete.html'
    success_url = reverse_lazy('supply_list')
    permission_required = 'inventory.can_edit_supply'

class LocationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Location
    template_name = 'inventory/location_list.html'
    context_object_name = 'locations'
    permission_required = 'inventory.view_location'

class LocationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'inventory/location_form.html'
    success_url = reverse_lazy('location_list')
    permission_required = 'inventory.add_location'

    def form_valid(self, form):
        messages.success(self.request, 'Location created successfully!')
        return super().form_valid(form)

class LocationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'inventory/location_form.html'
    success_url = reverse_lazy('location_list')
    permission_required = 'inventory.change_location'

    def form_valid(self, form):
        messages.success(self.request, 'Location updated successfully!')
        return super().form_valid(form)

class LocationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Location
    template_name = 'inventory/location_confirm_delete.html'
    success_url = reverse_lazy('location_list')
    permission_required = 'inventory.delete_location'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Location deleted successfully!')
        return super().delete(request, *args, **kwargs)
