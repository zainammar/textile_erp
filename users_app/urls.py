from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('roles-permissions/', views.roles_permissions, name='roles_permissions'),
    path('staff-management/', views.staff_management, name='staff_management'),
]
