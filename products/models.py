from decimal import Decimal
from django.db import models


class NamedMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        return self.name


class FabricCategory(NamedMaster):
    class Meta(NamedMaster.Meta):
        verbose_name_plural = "fabric categories"


class FabricQuality(NamedMaster):
    class Meta(NamedMaster.Meta):
        verbose_name_plural = "fabric qualities"


class Color(NamedMaster):
    pass


class Design(NamedMaster):
    pass


class Unit(NamedMaster):
    short = models.CharField(max_length=10)  # m, kg, yd ...

    def __str__(self):
        return self.short or self.name


class Gsm(models.Model):
    value = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ["value"]
        verbose_name = "GSM"
        verbose_name_plural = "GSM"

    def __str__(self):
        return f"{self.value} GSM"


class Width(models.Model):
    value = models.DecimalField(max_digits=6, decimal_places=2, unique=True)

    class Meta:
        ordering = ["value"]

    def __str__(self):
        return f'{Decimal(self.value).normalize():f}"'


class Fabric(models.Model):
    """Stock ki asal item: masters ka ek combination."""
    category = models.ForeignKey(FabricCategory, on_delete=models.PROTECT)
    quality = models.ForeignKey(FabricQuality, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    design = models.ForeignKey(Design, on_delete=models.PROTECT, null=True, blank=True)
    gsm = models.ForeignKey(Gsm, on_delete=models.PROTECT)
    width = models.ForeignKey(Width, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    class Meta:
        ordering = ["category__name", "quality__name", "color__name"]
        unique_together = [("category", "quality", "color", "design", "gsm", "width")]

    def __str__(self):
        parts = [str(self.category), str(self.quality), str(self.color)]
        if self.design:
            parts.append(str(self.design))
        parts += [str(self.gsm), str(self.width)]
        return " / ".join(parts)
