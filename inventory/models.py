from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Supply(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='supplies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_view_supply", "Can view supply"),
            ("can_edit_supply", "Can edit supply"),
        ]

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
    ]
    
    supply = models.ForeignKey(Supply, on_delete=models.SET_NULL, null=True, related_name='transactions')
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.supply.name if self.supply else 'Deleted Supply'} - {self.transaction_type} - {self.quantity}"

class StockAlert(models.Model):
    ALERT_TYPES = [
        ('low_stock', 'Low Stock'),
        ('out_of_stock', 'Out of Stock'),
    ]
    
    supply = models.ForeignKey(Supply, on_delete=models.SET_NULL, null=True, related_name='alerts')
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.supply.name if self.supply else 'Deleted Supply'} - {self.alert_type}"

class AlertConfig(models.Model):
    ALERT_TYPES = [
        ('low_stock', 'Low Stock'),
        ('out_of_stock', 'Out of Stock'),
    ]
    
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES, unique=True)
    threshold = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.alert_type} - {self.threshold}"
