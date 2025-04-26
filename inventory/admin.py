from django.contrib import admin
from .models import Product, Location

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'quantity', 'location')
    list_filter = ('location',)
    search_fields = ('sku', 'name')
    ordering = ('location', 'name')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'created_at', 'updated_at')
    search_fields = ('code', 'name')
    ordering = ('code',)
