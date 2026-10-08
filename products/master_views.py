"""Masters (category, quality, color ...) ke list/add/edit/delete pages ek jagah se."""
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def master_urls(model, name, slug, title, columns, fields):
    success = reverse_lazy(f"products:{name}")

    class Base:
        success_url = success

        def get_context_data(self, **kw):
            ctx = super().get_context_data(**kw)
            ctx.update(name=name, title=title)
            return ctx

    class L(Base, ListView):
        template_name = "products/master_list.html"
        paginate_by = 20

        def get_queryset(self):
            return model.objects.all()

        def get_context_data(self, **kw):
            ctx = super().get_context_data(**kw)
            rows = []
            for o in ctx["object_list"]:
                vals = []
                for _, attr in columns:
                    v = getattr(o, attr)
                    vals.append(v() if callable(v) else v)
                rows.append((o, vals))
            ctx["headers"] = [h for h, _ in columns]
            ctx["rows"] = rows
            return ctx

    class C(Base, CreateView):
        template_name = "products/master_form.html"

    class U(Base, UpdateView):
        template_name = "products/master_form.html"

    class D(Base, DeleteView):
        template_name = "products/master_confirm_delete.html"

        def form_valid(self, form):
            try:
                return super().form_valid(form)
            except ProtectedError:
                messages.error(self.request, "Ye record kahin istemal ho raha hai, delete nahi ho sakta.")
                return redirect(success)

    C.model = U.model = D.model = L.model = model
    C.fields = U.fields = fields
    return [
        path(f"{slug}/", L.as_view(), name=name),
        path(f"{slug}/add/", C.as_view(), name=f"{name}_add"),
        path(f"{slug}/<int:pk>/edit/", U.as_view(), name=f"{name}_edit"),
        path(f"{slug}/<int:pk>/delete/", D.as_view(), name=f"{name}_delete"),
    ]
