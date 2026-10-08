from django.views.generic import ListView
from .models import StockBalance, StockMovement


class StockList(ListView):
    model = StockBalance
    paginate_by = 20
    template_name = "inventory/stock_list.html"

    def get_queryset(self):
        return StockBalance.objects.select_related(
            "fabric__category", "fabric__quality", "fabric__color", "fabric__gsm",
            "fabric__width", "fabric__unit")


class MovementList(ListView):
    model = StockMovement
    paginate_by = 20
    template_name = "inventory/movement_list.html"

    def get_queryset(self):
        qs = StockMovement.objects.select_related("fabric")
        d = self.request.GET.get("dir")
        return qs.filter(direction=d) if d in ("in", "out") else qs
