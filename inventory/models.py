from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)  # Item
    sku = models.CharField(max_length=50, unique=True, default=uuid.uuid4)  # SKU
    quantity = models.IntegerField()  # Count
    aisle = models.CharField(max_length=50)  # Aisle
    bay = models.CharField(max_length=50, default='A1')  # Bay
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

    class Meta:
        ordering = ['aisle', 'bay']
