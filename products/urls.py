from .master_views import master_urls
from .models import (FabricCategory, FabricQuality, Color, Design, Unit, Gsm, Width, Fabric)

app_name = "products"

NAMED = [("Name", "name"), ("Active", "is_active")]

urlpatterns = (
    master_urls(FabricCategory, "fabric_category", "fabric-category", "Fabric Category", NAMED, ["name", "is_active"])
    + master_urls(FabricQuality, "fabric_quality", "fabric-quality", "Fabric Quality", NAMED, ["name", "is_active"])
    + master_urls(Color, "color", "color", "Color", NAMED, ["name", "is_active"])
    + master_urls(Design, "design", "design", "Design", NAMED, ["name", "is_active"])
    + master_urls(Gsm, "gsm", "gsm", "GSM", [("GSM", "value")], ["value"])
    + master_urls(Width, "width", "width", "Width", [("Width", "value")], ["value"])
    + master_urls(Unit, "unit", "unit", "Unit", [("Name", "name"), ("Short", "short")], ["name", "short", "is_active"])
    + master_urls(Fabric, "fabric", "fabric", "Fabrics",
                  [("Fabric", "__str__"), ("Unit", "unit")],
                  ["category", "quality", "color", "design", "gsm", "width", "unit"])
)
