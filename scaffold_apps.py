"""
One-time scaffolding script: generates urls.py + views.py for every app
based on the menu structure, using a shared placeholder template.
Run once: python scaffold_apps.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

MENU = {
    "customers": [
        ("add-customer", "Add Customer"),
        ("ledger", "Customer Ledger"),
        ("payment-history", "Payment History"),
    ],
    "suppliers": [
        ("add-supplier", "Add Supplier"),
        ("purchase-history", "Purchase History"),
        ("ledger", "Supplier Ledger"),
    ],
    "products": [
        ("fabric-category", "Fabric Category"),
        ("fabric-quality", "Fabric Quality"),
        ("color", "Color"),
        ("design", "Design"),
        ("gsm", "GSM"),
        ("width", "Width"),
        ("unit", "Unit"),
    ],
    "inventory": [
        ("stock-in", "Stock In"),
        ("stock-out", "Stock Out"),
        ("stock-adjustment", "Stock Adjustment"),
        ("warehouse", "Warehouse Management"),
    ],
    "purchase": [
        ("orders", "Purchase Orders"),
        ("receive-goods", "Receive Goods"),
        ("invoice", "Purchase Invoice"),
    ],
    "sales": [
        ("order", "Sales Order"),
        ("invoice", "Sales Invoice"),
        ("delivery-challan", "Delivery Challan"),
        ("return-management", "Return Management"),
    ],
    "accounts": [
        ("income", "Income"),
        ("expense", "Expense"),
        ("cash-book", "Cash Book"),
        ("bank-book", "Bank Book"),
        ("customer-ledger", "Customer Ledger"),
        ("supplier-ledger", "Supplier Ledger"),
    ],
    "reports_app": [
        ("sales-report", "Sales Report"),
        ("purchase-report", "Purchase Report"),
        ("stock-report", "Stock Report"),
        ("profit-loss", "Profit & Loss"),
        ("customer-report", "Customer Report"),
        ("supplier-report", "Supplier Report"),
    ],
    "users_app": [
        ("roles-permissions", "Roles & Permissions"),
        ("staff-management", "Staff Management"),
    ],
    "company_settings": [
        ("company-info", "Company Information"),
        ("invoice-settings", "Invoice Settings"),
        ("tax", "Tax"),
        ("currency", "Currency"),
    ],
}

VIEWS_HEADER = """from django.contrib.auth.decorators import login_required
from django.shortcuts import render


"""

VIEW_FUNC_TEMPLATE = """@login_required
def {func_name}(request):
    return render(request, 'module_placeholder.html', {{
        'module_title': '{app_label}',
        'page_title': '{page_title}',
    }})

"""

URLS_HEADER = """from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
"""

for app, items in MENU.items():
    app_label = app.replace("_app", "").replace("_", " ").title()
    views_path = os.path.join(BASE, app, "views.py")
    urls_path = os.path.join(BASE, app, "urls.py")

    with open(views_path, "w") as f:
        f.write(VIEWS_HEADER)
        for slug, label in items:
            func_name = slug.replace("-", "_")
            f.write(VIEW_FUNC_TEMPLATE.format(
                func_name=func_name, app_label=app_label, page_title=label
            ))

    with open(urls_path, "w") as f:
        f.write(URLS_HEADER.format(app_name=app))
        for slug, label in items:
            func_name = slug.replace("-", "_")
            f.write(f"    path('{slug}/', views.{func_name}, name='{func_name}'),\n")
        f.write("]\n")

    print(f"Scaffolded {app}: {len(items)} pages")

print("Done.")
