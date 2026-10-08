from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models, transaction
from products.models import Fabric


class StockBalance(models.Model):
    fabric = models.OneToOneField(Fabric, on_delete=models.CASCADE, related_name="balance")
    quantity = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["fabric__category__name"]

    def __str__(self):
        return f"{self.fabric}: {self.quantity}"


class StockMovement(models.Model):
    IN, OUT = "in", "out"
    DIRECTIONS = [(IN, "Stock In"), (OUT, "Stock Out")]
    REASONS = [
        ("opening", "Opening stock"), ("production", "Production"), ("purchase", "Purchase"),
        ("sale", "Sale"), ("adjustment", "Adjustment"), ("reversal", "Reversal"),
    ]

    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT, related_name="movements")
    direction = models.CharField(max_length=3, choices=DIRECTIONS)
    quantity = models.DecimalField(max_digits=14, decimal_places=2)  # hamesha positive
    reason = models.CharField(max_length=12, choices=REASONS, default="adjustment")
    reference = models.CharField(max_length=40, blank=True)          # e.g. PO-0003
    note = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    @property
    def delta(self):
        return self.quantity if self.direction == self.IN else -self.quantity

    def clean(self):
        if self.quantity is not None and self.quantity <= 0:
            raise ValidationError("Quantity 0 se zyada honi chahiye.")
        if self.pk is None and self.direction == self.OUT and self.fabric_id:
            bal = StockBalance.objects.filter(fabric_id=self.fabric_id).first()
            if (bal.quantity if bal else Decimal(0)) < (self.quantity or 0):
                raise ValidationError("Itna stock maujood nahi hai.")

    @transaction.atomic
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:  # balance sirf naye movement par update hota hai
            bal, _ = StockBalance.objects.select_for_update().get_or_create(fabric_id=self.fabric_id)
            bal.quantity += self.delta
            bal.save()

    def __str__(self):
        return f"{self.get_direction_display()} {self.quantity} - {self.fabric}"
