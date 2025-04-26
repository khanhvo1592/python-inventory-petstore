from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('low-stock/', views.low_stock_view, name='low_stock'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('users/', views.user_management, name='user_management'),
    
    # Location URLs
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('locations/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/update/', views.LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),
    
    path('supplies/', views.SupplyListView.as_view(), name='supply_list'),
    path('supplies/create/', views.SupplyCreateView.as_view(), name='supply_create'),
    path('supplies/<int:pk>/update/', views.SupplyUpdateView.as_view(), name='supply_update'),
    path('supplies/<int:pk>/delete/', views.SupplyDeleteView.as_view(), name='supply_delete'),
] 