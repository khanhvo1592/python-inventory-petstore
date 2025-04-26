from django.db import models
import uuid

# Create your models here.

class Location(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ['code']

class Supply(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='supplies')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

    class Meta:
        ordering = ['location', 'name']
        permissions = [
            ("can_view_supply", "Can view supply"),
            ("can_edit_supply", "Can edit supply"),
        ]

class Product(models.Model):
    name = models.CharField(max_length=100)  # Item
    sku = models.CharField(max_length=50, unique=True, default=uuid.uuid4)  # SKU
    quantity = models.IntegerField()  # Count
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='products')  # Location
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

    class Meta:
        ordering = ['location', 'name']
        permissions = [
            ("can_view_product", "Can view product"),
            ("can_edit_product", "Can edit product"),
        ]
