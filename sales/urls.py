from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('order/', views.order, name='order'),
    path('invoice/', views.invoice, name='invoice'),
    path('delivery-challan/', views.delivery_challan, name='delivery_challan'),
    path('return-management/', views.return_management, name='return_management'),
]
