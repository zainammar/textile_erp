from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def stock_in(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Inventory',
        'page_title': 'Stock In',
    })

@login_required
def stock_out(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Inventory',
        'page_title': 'Stock Out',
    })

@login_required
def stock_adjustment(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Inventory',
        'page_title': 'Stock Adjustment',
    })

@login_required
def warehouse(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Inventory',
        'page_title': 'Warehouse Management',
    })

