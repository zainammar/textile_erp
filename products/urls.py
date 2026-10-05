from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('fabric-category/', views.fabric_category, name='fabric_category'),
    path('fabric-quality/', views.fabric_quality, name='fabric_quality'),
    path('color/', views.color, name='color'),
    path('design/', views.design, name='design'),
    path('gsm/', views.gsm, name='gsm'),
    path('width/', views.width, name='width'),
    path('unit/', views.unit, name='unit'),
]
