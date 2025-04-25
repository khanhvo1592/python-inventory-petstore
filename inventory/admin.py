from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'quantity', 'aisle', 'bay')
    list_filter = ('aisle', 'bay')
    search_fields = ('sku', 'name', 'aisle', 'bay')
    ordering = ('aisle', 'bay')
