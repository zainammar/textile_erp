from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('income/', views.income, name='income'),
    path('expense/', views.expense, name='expense'),
    path('cash-book/', views.cash_book, name='cash_book'),
    path('bank-book/', views.bank_book, name='bank_book'),
    path('customer-ledger/', views.customer_ledger, name='customer_ledger'),
    path('supplier-ledger/', views.supplier_ledger, name='supplier_ledger'),
]
