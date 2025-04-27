from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from .models import Supply, Location, StockTransaction, StockAlert, AlertConfig
from .forms import (
    LocationForm, 
    SupplyForm, 
    UserForm, 
    StockTransactionForm,
    StockAlertForm,
    AlertConfigForm
)
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Sum, Count, F, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.views import View

# Supply Views
class SupplyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supply
    template_name = 'inventory/supply_list.html'
    context_object_name = 'supplies'
    permission_required = 'inventory.can_view_supply'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context

class SupplyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Supply
    form_class = SupplyForm
    template_name = 'inventory/supply_form.html'
    success_url = reverse_lazy('inventory:supply_list')
    permission_required = 'inventory.can_edit_supply'

    def form_valid(self, form):
        messages.success(self.request, 'Supply created successfully!')
        return super().form_valid(form)

class SupplyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supply
    form_class = SupplyForm
    template_name = 'inventory/supply_form.html'
    success_url = reverse_lazy('inventory:supply_list')
    permission_required = 'inventory.can_edit_supply'

    def form_valid(self, form):
        messages.success(self.request, 'Supply updated successfully!')
        return super().form_valid(form)

class SupplyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supply
    template_name = 'inventory/supply_confirm_delete.html'
    success_url = reverse_lazy('inventory:supply_list')
    permission_required = 'inventory.can_edit_supply'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Supply deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Location Views
class LocationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Location
    template_name = 'inventory/location_list.html'
    context_object_name = 'locations'
    permission_required = 'inventory.view_location'

class LocationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'inventory/location_form.html'
    success_url = reverse_lazy('inventory:location_list')
    permission_required = 'inventory.add_location'

    def form_valid(self, form):
        messages.success(self.request, 'Location created successfully!')
        return super().form_valid(form)

class LocationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'inventory/location_form.html'
    success_url = reverse_lazy('inventory:location_list')
    permission_required = 'inventory.change_location'

    def form_valid(self, form):
        messages.success(self.request, 'Location updated successfully!')
        return super().form_valid(form)

class LocationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Location
    template_name = 'inventory/location_confirm_delete.html'
    success_url = reverse_lazy('inventory:location_list')
    permission_required = 'inventory.delete_location'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Location deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Stock Transaction Views
class StockTransactionListView(LoginRequiredMixin, ListView):
    model = StockTransaction
    template_name = 'inventory/transaction_list.html'
    context_object_name = 'transactions'

class StockTransactionCreateView(LoginRequiredMixin, CreateView):
    model = StockTransaction
    form_class = StockTransactionForm
    template_name = 'inventory/transaction_form.html'
    success_url = reverse_lazy('inventory:transaction_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Transaction created successfully!')
        return super().form_valid(form)

class StockTransactionDetailView(LoginRequiredMixin, DetailView):
    model = StockTransaction
    template_name = 'inventory/transaction_detail.html'
    context_object_name = 'transaction'

# Stock Alert Views
class StockAlertListView(LoginRequiredMixin, ListView):
    model = StockAlert
    template_name = 'inventory/alert_list.html'
    context_object_name = 'alerts'

class StockAlertMarkReadView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        alert = get_object_or_404(StockAlert, pk=kwargs['pk'])
        alert.is_read = True
        alert.save()
        messages.success(request, 'Alert marked as read!')
        return redirect('inventory:alert_list')

class StockAlertDeleteView(LoginRequiredMixin, DeleteView):
    model = StockAlert
    template_name = 'inventory/alert_confirm_delete.html'
    success_url = reverse_lazy('inventory:alert_list')

# Alert Config Views
class AlertConfigListView(LoginRequiredMixin, ListView):
    model = AlertConfig
    template_name = 'inventory/alert_config_list.html'
    context_object_name = 'alert_configs'

class AlertConfigCreateView(LoginRequiredMixin, CreateView):
    model = AlertConfig
    form_class = AlertConfigForm
    template_name = 'inventory/alert_config_form.html'
    success_url = reverse_lazy('inventory:alert_config_list')

class AlertConfigUpdateView(LoginRequiredMixin, UpdateView):
    model = AlertConfig
    form_class = AlertConfigForm
    template_name = 'inventory/alert_config_form.html'
    success_url = reverse_lazy('inventory:alert_config_list')

class AlertConfigDeleteView(LoginRequiredMixin, DeleteView):
    model = AlertConfig
    template_name = 'inventory/alert_config_confirm_delete.html'
    success_url = reverse_lazy('inventory:alert_config_list')

# User Views
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'inventory/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'inventory/user_form.html'
    success_url = reverse_lazy('inventory:user_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'inventory/user_form.html'
    success_url = reverse_lazy('inventory:user_list')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'inventory/user_confirm_delete.html'
    success_url = reverse_lazy('inventory:user_list')

# Dashboard and Stats Views
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Stock Statistics
        total_supplies = Supply.objects.count()
        low_stock_supplies = Supply.objects.filter(quantity__lt=10).count()
        out_of_stock_supplies = Supply.objects.filter(quantity=0).count()
        
        # Recent Transactions
        recent_transactions = StockTransaction.objects.select_related('supply').order_by('-created_at')[:10]
        
        # Stock Alerts
        unread_alerts = StockAlert.objects.filter(is_read=False).select_related('supply')
        
        # Monthly Stock Movement
        monthly_movement = StockTransaction.objects.annotate(
            month=TruncMonth('created_at')
        ).values('month', 'transaction_type').annotate(
            total_quantity=Sum('quantity')
        ).order_by('month')
        
        context.update({
            'total_supplies': total_supplies,
            'low_stock_supplies': low_stock_supplies,
            'out_of_stock_supplies': out_of_stock_supplies,
            'recent_transactions': recent_transactions,
            'unread_alerts': unread_alerts,
            'monthly_movement': monthly_movement,
        })
        return context

class StockReportView(LoginRequiredMixin, ListView):
    template_name = 'inventory/stock_report.html'
    context_object_name = 'supplies'
    model = Supply

    def get_queryset(self):
        return Supply.objects.annotate(
            total_in=Sum('transactions__quantity', filter=Q(transactions__transaction_type='in')),
            total_out=Sum('transactions__quantity', filter=Q(transactions__transaction_type='out'))
        ).order_by('name')

class AlertSettingsView(LoginRequiredMixin, ListView):
    template_name = 'inventory/alert_settings.html'
    model = AlertConfig
    context_object_name = 'alert_configs'

    def post(self, request, *args, **kwargs):
        alert_type = request.POST.get('alert_type')
        threshold = request.POST.get('threshold')
        is_active = request.POST.get('is_active') == 'on'
        
        config, created = AlertConfig.objects.update_or_create(
            alert_type=alert_type,
            defaults={'threshold': threshold, 'is_active': is_active}
        )
        
        messages.success(request, 'Alert settings updated successfully!')
        return redirect('inventory:alert_settings')

def check_stock_alerts():
    # Get active alert configurations
    alert_configs = AlertConfig.objects.filter(is_active=True)
    
    for config in alert_configs:
        if config.alert_type == 'low_stock':
            # Find supplies with quantity below threshold
            low_stock_supplies = Supply.objects.filter(quantity__lt=config.threshold)
            
            for supply in low_stock_supplies:
                # Check if alert already exists and is unread
                existing_alert = StockAlert.objects.filter(
                    supply=supply,
                    alert_type='low_stock',
                    is_read=False
                ).exists()
                
                if not existing_alert:
                    # Create new alert
                    StockAlert.objects.create(
                        supply=supply,
                        alert_type='low_stock',
                        message=f"Low stock alert: {supply.name} has only {supply.quantity} units remaining (threshold: {config.threshold})"
                    )
        
        elif config.alert_type == 'out_of_stock':
            # Find supplies with zero quantity
            out_of_stock_supplies = Supply.objects.filter(quantity=0)
            
            for supply in out_of_stock_supplies:
                # Check if alert already exists and is unread
                existing_alert = StockAlert.objects.filter(
                    supply=supply,
                    alert_type='out_of_stock',
                    is_read=False
                ).exists()
                
                if not existing_alert:
                    # Create new alert
                    StockAlert.objects.create(
                        supply=supply,
                        alert_type='out_of_stock',
                        message=f"Out of stock alert: {supply.name} has 0 units remaining"
                    )

@login_required
def low_stock_alert(request):
    low_stock_supplies = Supply.objects.filter(quantity__lt=10)
    return render(request, 'inventory/supply_list.html', {'supplies': low_stock_supplies})

@login_required
def stats_view(request):
    # Get statistics
    total_supplies = Supply.objects.count()
    total_locations = Location.objects.count()
    total_users = User.objects.count()
    
    # Get low stock supplies
    low_stock_supplies = Supply.objects.filter(quantity__lt=10)
    
    context = {
        'total_supplies': total_supplies,
        'total_locations': total_locations,
        'total_users': total_users,
        'low_stock_supplies': low_stock_supplies,
    }
    
    return render(request, 'inventory/stats.html', context)

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return render(request, 'inventory/logout.html')

@login_required
def user_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('inventory:supply_list')
    
    users = User.objects.all().order_by('username')
    return render(request, 'inventory/user_management.html', {'users': users})
