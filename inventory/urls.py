from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # Location URLs
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('locations/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/update/', views.LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),

    # Supply URLs
    path('', views.SupplyListView.as_view(), name='supply_list'),
    path('supplies/create/', views.SupplyCreateView.as_view(), name='supply_create'),
    path('supplies/<int:pk>/update/', views.SupplyUpdateView.as_view(), name='supply_update'),
    path('supplies/<int:pk>/delete/', views.SupplyDeleteView.as_view(), name='supply_delete'),

    # Stock Transaction URLs
    path('transactions/', views.StockTransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/', views.StockTransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/', views.StockTransactionDetailView.as_view(), name='transaction_detail'),

    # Stock Alert URLs
    path('alerts/', views.StockAlertListView.as_view(), name='alert_list'),
    path('alerts/<int:pk>/mark-read/', views.StockAlertMarkReadView.as_view(), name='alert_mark_read'),
    path('alerts/<int:pk>/delete/', views.StockAlertDeleteView.as_view(), name='alert_delete'),

    # Alert Config URLs
    path('alert-configs/', views.AlertConfigListView.as_view(), name='alert_config_list'),
    path('alert-configs/create/', views.AlertConfigCreateView.as_view(), name='alert_config_create'),
    path('alert-configs/<int:pk>/update/', views.AlertConfigUpdateView.as_view(), name='alert_config_update'),
    path('alert-configs/<int:pk>/delete/', views.AlertConfigDeleteView.as_view(), name='alert_config_delete'),

    # User URLs
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
] 