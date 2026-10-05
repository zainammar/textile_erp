from django.urls import path
from . import views

app_name = 'suppliers'

urlpatterns = [
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('purchase-history/', views.purchase_history, name='purchase_history'),
    path('ledger/', views.ledger, name='ledger'),
]
