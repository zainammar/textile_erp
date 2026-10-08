from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from .forms import UserForm
from .models import Profile

User = get_user_model()


class AdminOnly(LoginRequiredMixin, UserPassesTestMixin):
    """Sirf superuser ya Admin role wale users."""
    def test_func(self):
        u = self.request.user
        if u.is_superuser:
            return True
        p = getattr(u, "profile", None)
        return bool(p and p.role == Profile.ADMIN)


class UserList(AdminOnly, ListView):
    model = User
    paginate_by = 20
    template_name = "users_app/list.html"

    def get_queryset(self):
        qs = User.objects.select_related("profile").order_by("username")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(Q(username__icontains=q) | Q(first_name__icontains=q)
                           | Q(last_name__icontains=q) | Q(email__icontains=q))
        return qs

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        ctx["q"] = self.request.GET.get("q", "")
        return ctx


class UserCreate(AdminOnly, CreateView):
    model = User
    form_class = UserForm
    template_name = "users_app/form.html"
    success_url = reverse_lazy("users_app:list")


class UserUpdate(AdminOnly, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users_app/form.html"
    success_url = reverse_lazy("users_app:list")


class UserToggle(AdminOnly, View):
    """Delete ki jagah active/inactive."""
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user.pk == request.user.pk:
            messages.error(request, "Apna account inactive nahi kar sakte.")
        else:
            user.is_active = not user.is_active
            user.save(update_fields=["is_active"])
        return redirect("users_app:list")


class RolesPermissions(AdminOnly, TemplateView):
    """Roles ki list, har role mein kitne users hain, aur unka access (abhi sirf dikhane ke liye)."""
    template_name = "users_app/roles.html"

    ACCESS = {
        Profile.ADMIN: "Tamam modules + Users",
        Profile.MANAGER: "Production, Inventory, Purchase, Sales, Reports",
        Profile.STORE: "Inventory, Stock, Production",
        Profile.SALES: "Customers, Sales",
        Profile.ACCOUNTS: "Accounts, Reports, Purchase, Sales (sirf dekhna)",
    }

    def get_context_data(self, **kw):
        ctx = super().get_context_data(**kw)
        rows = []
        for code, label in Profile.ROLES:
            users = [p.user for p in Profile.objects.filter(role=code).select_related("user")]
            rows.append({"label": label, "access": self.ACCESS.get(code, ""), "users": users})
        ctx["rows"] = rows
        return ctx
