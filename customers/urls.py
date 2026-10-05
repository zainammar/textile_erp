from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('add-customer/', views.add_customer, name='add_customer'),
    path('ledger/', views.ledger, name='ledger'),
    path('payment-history/', views.payment_history, name='payment_history'),
]
