"""Baqi apps stock yahan se hi hilayen (production, purchase, sales)."""
from decimal import Decimal
from django.db import transaction
from .models import StockBalance, StockMovement


class InsufficientStock(Exception):
    pass


@transaction.atomic
def stock_in(fabric, qty, reason, reference="", note=""):
    return StockMovement.objects.create(
        fabric=fabric, direction=StockMovement.IN, quantity=qty,
        reason=reason, reference=reference, note=note)


@transaction.atomic
def stock_out(fabric, qty, reason, reference="", note="", allow_negative=False):
    if not allow_negative:
        bal = StockBalance.objects.filter(fabric=fabric).first()
        if (bal.quantity if bal else Decimal(0)) < qty:
            raise InsufficientStock(f"{fabric}: itna stock nahi hai")
    return StockMovement.objects.create(
        fabric=fabric, direction=StockMovement.OUT, quantity=qty,
        reason=reason, reference=reference, note=note)
