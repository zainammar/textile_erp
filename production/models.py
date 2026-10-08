from django.db import models, transaction
from products.models import Fabric


class ProductionOrder(models.Model):
    PENDING, IN_PROGRESS, COMPLETED, CANCELLED = "pending", "in_progress", "completed", "cancelled"
    STATUS = [
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    ]

    buyer = models.CharField(max_length=120, default="")
    # null=True sirf purane rows ke liye; form mein required hai
    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT, null=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS, default=PENDING)
    notes = models.TextField(blank=True)
    stock_added = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    @property
    def order_no(self):
        return f"PO-{self.pk:04d}"

    @transaction.atomic
    def save(self, *args, **kwargs):
        from inventory.services import stock_in, stock_out
        super().save(*args, **kwargs)  # pehle pk chahiye (reference ke liye)
        if not self.fabric_id:
            return
        if self.status == self.COMPLETED and not self.stock_added:
            stock_in(self.fabric, self.quantity, "production", self.order_no)
            self._flag(True)
        elif self.status != self.COMPLETED and self.stock_added:
            stock_out(self.fabric, self.quantity, "reversal", self.order_no,
                      "Status Completed se hata", allow_negative=True)
            self._flag(False)

    @transaction.atomic
    def delete(self, *args, **kwargs):
        from inventory.services import stock_out
        if self.stock_added and self.fabric_id:
            stock_out(self.fabric, self.quantity, "reversal", self.order_no,
                      "Order delete hua", allow_negative=True)
        return super().delete(*args, **kwargs)

    def _flag(self, value):
        self.stock_added = value
        type(self).objects.filter(pk=self.pk).update(stock_added=value)

    def __str__(self):
        return f"{self.order_no} - {self.fabric}"
