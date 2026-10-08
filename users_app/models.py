from django.conf import settings
from django.db import models


class Profile(models.Model):
    """Django ke built-in User ke saath extra info (phone, role)."""
    ADMIN, MANAGER, STORE, SALES, ACCOUNTS = "admin", "manager", "store", "sales", "accounts"
    ROLES = [
        (ADMIN, "Admin"),
        (MANAGER, "Manager"),
        (STORE, "Store / Inventory"),
        (SALES, "Sales"),
        (ACCOUNTS, "Accounts"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=10, choices=ROLES, default=SALES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        return f"{self.user.get_username()} ({self.get_role_display()})"
