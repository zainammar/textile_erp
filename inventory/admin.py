from django.contrib import admin
from .models import StockBalance, StockMovement


@admin.register(StockBalance)
class StockBalanceAdmin(admin.ModelAdmin):
    list_display = ("fabric", "quantity", "updated")
    readonly_fields = ("fabric", "quantity")

    def has_add_permission(self, request):
        return False


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ("created", "fabric", "direction", "quantity", "reason", "reference")
    list_filter = ("direction", "reason")

    def has_change_permission(self, request, obj=None):
        return obj is None

    def has_delete_permission(self, request, obj=None):
        return False
