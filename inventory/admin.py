from django.contrib import admin
from .models import Supply, Location, StockTransaction, StockAlert, AlertConfig

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'location', 'created_at', 'updated_at')
    list_filter = ('location',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('supply', 'quantity', 'transaction_type', 'created_by', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    search_fields = ('supply__name', 'notes')
    ordering = ('-created_at',)

@admin.register(StockAlert)
class StockAlertAdmin(admin.ModelAdmin):
    list_display = ('supply', 'alert_type', 'is_read', 'created_at')
    list_filter = ('alert_type', 'is_read', 'created_at')
    search_fields = ('supply__name', 'message')
    ordering = ('-created_at',)

@admin.register(AlertConfig)
class AlertConfigAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'threshold', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    ordering = ('alert_type',)
