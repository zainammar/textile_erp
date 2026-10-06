from django.db import models


class ProductionOrder(models.Model):
    """Self-contained: koi dusre app ka model import nahi karta."""
    PENDING, IN_PROGRESS, COMPLETED, CANCELLED = "pending", "in_progress", "completed", "cancelled"
    STATUS = [
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    ]
    UNITS = [("m", "Meter"), ("yd", "Yard"), ("kg", "Kg"), ("thaan", "Thaan")]

    # Fabric specs (baad mein products ke masters ki ForeignKey bana sakte hain)
    fabric_category = models.CharField(max_length=80)
    quality = models.CharField(max_length=80, blank=True)
    color = models.CharField(max_length=60, blank=True)
    design = models.CharField(max_length=80, blank=True)
    gsm = models.PositiveIntegerField("GSM", null=True, blank=True)
    width = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNITS, default="m")
    start_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS, default=PENDING)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    @property
    def order_no(self):
        return f"PO-{self.pk:04d}"

    def __str__(self):
        return f"{self.order_no} - {self.fabric_category}"
