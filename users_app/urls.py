from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path("", views.UserList.as_view(), name="list"),
    path("staff/", views.UserList.as_view(), name="staff_management"),
    path("roles/", views.RolesPermissions.as_view(), name="roles_permissions"),
    path("add/", views.UserCreate.as_view(), name="add"),
    path("<int:pk>/edit/", views.UserUpdate.as_view(), name="edit"),
    path("<int:pk>/toggle/", views.UserToggle.as_view(), name="toggle"),
]
