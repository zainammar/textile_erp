from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    # NOTE: placeholder static numbers. Connect real querysets from
    # sales / purchase / inventory / accounts apps once those models exist.
    context = {
        'sales_summary': {'today': 0, 'this_month': 0, 'total': 0},
        'purchase_summary': {'today': 0, 'this_month': 0, 'total': 0},
        'stock_summary': {'total_items': 0, 'low_stock': 0},
        'profit_report': {'this_month': 0},
        'recent_orders': [],
    }
    return render(request, 'core/dashboard.html', context)
