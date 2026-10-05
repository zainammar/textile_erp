from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('stock-in/', views.stock_in, name='stock_in'),
    path('stock-out/', views.stock_out, name='stock_out'),
    path('stock-adjustment/', views.stock_adjustment, name='stock_adjustment'),
    path('warehouse/', views.warehouse, name='warehouse'),
]
