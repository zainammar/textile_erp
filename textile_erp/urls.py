"""textile_erp URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Modules
    path('', include('core.urls')),
    path('customers/', include('customers.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('products/', include('products.urls')),
    path('inventory/', include('inventory.urls')),
    path('purchase/', include('purchase.urls')),
    path('sales/', include('sales.urls')),
    path('accounts/', include('accounts.urls')),
    path('reports/', include('reports_app.urls')),
    path('users/', include('users_app.urls')),
    path('settings/', include('company_settings.urls')),
]
