from django.urls import path
from . import views

app_name = 'reports_app'

urlpatterns = [
    path('sales-report/', views.sales_report, name='sales_report'),
    path('purchase-report/', views.purchase_report, name='purchase_report'),
    path('stock-report/', views.stock_report, name='stock_report'),
    path('profit-loss/', views.profit_loss, name='profit_loss'),
    path('customer-report/', views.customer_report, name='customer_report'),
    path('supplier-report/', views.supplier_report, name='supplier_report'),
]
