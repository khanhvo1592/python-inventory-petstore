from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Supply, Location, StockTransaction, StockAlert, AlertConfig

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['name', 'quantity', 'price', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ['supply', 'quantity', 'transaction_type', 'notes']
        widgets = {
            'supply': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class StockAlertForm(forms.ModelForm):
    class Meta:
        model = StockAlert
        fields = ['supply', 'alert_type', 'message', 'is_read']
        widgets = {
            'supply': forms.Select(attrs={'class': 'form-control'}),
            'alert_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_read': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AlertConfigForm(forms.ModelForm):
    class Meta:
        model = AlertConfig
        fields = ['alert_type', 'threshold', 'is_active']
        widgets = {
            'alert_type': forms.Select(attrs={'class': 'form-control'}),
            'threshold': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 