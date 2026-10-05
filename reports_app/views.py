from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def sales_report(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Reports',
        'page_title': 'Sales Report',
    })

@login_required
def purchase_report(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Reports',
        'page_title': 'Purchase Report',
    })

@login_required
def stock_report(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Reports',
        'page_title': 'Stock Report',
    })

@login_required
def profit_loss(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Reports',
        'page_title': 'Profit & Loss',
    })

@login_required
def customer_report(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Reports',
        'page_title': 'Customer Report',
    })

@login_required
def supplier_report(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Reports',
        'page_title': 'Supplier Report',
    })

