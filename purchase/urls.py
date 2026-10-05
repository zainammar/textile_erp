from django.urls import path
from . import views

app_name = 'purchase'

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('receive-goods/', views.receive_goods, name='receive_goods'),
    path('invoice/', views.invoice, name='invoice'),
]
