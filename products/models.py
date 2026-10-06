from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    UNITS = [("m", "Meter"), ("kg", "Kg"), ("pc", "Piece"), ("thaan", "Thaan")]
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=30, unique=True)
    unit = models.CharField(max_length=10, choices=UNITS, default="m")
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.code})"