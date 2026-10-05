from django.urls import path
from . import views

app_name = 'company_settings'

urlpatterns = [
    path('company-info/', views.company_info, name='company_info'),
    path('invoice-settings/', views.invoice_settings, name='invoice_settings'),
    path('tax/', views.tax, name='tax'),
    path('currency/', views.currency, name='currency'),
]
