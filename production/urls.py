from django.urls import path
from . import views

app_name = "production"

urlpatterns = [
    path("", views.OrderList.as_view(), name="list"),
    path("add/", views.OrderCreate.as_view(), name="add"),
    path("<int:pk>/edit/", views.OrderUpdate.as_view(), name="edit"),
    path("<int:pk>/delete/", views.OrderDelete.as_view(), name="delete"),
]
