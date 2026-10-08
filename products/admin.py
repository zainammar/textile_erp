from django.contrib import admin
from . import models

for m in (models.FabricCategory, models.FabricQuality, models.Color, models.Design,
          models.Unit, models.Gsm, models.Width):
    admin.site.register(m)


@admin.register(models.Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ("__str__", "unit")
    list_filter = ("category", "quality", "color")
