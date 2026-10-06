from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ProductionOrder

FIELDS = ["fabric_category", "quality", "color", "design", "gsm", "width",
          "quantity", "unit", "start_date", "due_date", "status", "notes"]


class OrderList(ListView):
    model = ProductionOrder
    paginate_by = 15
    template_name = "production/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get("status")
        return qs.filter(status=status) if status else qs

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx["statuses"] = ProductionOrder.STATUS
        ctx["current"] = self.request.GET.get("status", "")
        return ctx


class OrderCreate(CreateView):
    model = ProductionOrder
    fields = FIELDS
    template_name = "production/form.html"
    success_url = reverse_lazy("production:list")


class OrderUpdate(UpdateView):
    model = ProductionOrder
    fields = FIELDS
    template_name = "production/form.html"
    success_url = reverse_lazy("production:list")


class OrderDelete(DeleteView):
    model = ProductionOrder
    template_name = "production/confirm_delete.html"
    success_url = reverse_lazy("production:list")
