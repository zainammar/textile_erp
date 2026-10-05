from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def add_supplier(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Suppliers',
        'page_title': 'Add Supplier',
    })

@login_required
def purchase_history(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Suppliers',
        'page_title': 'Purchase History',
    })

@login_required
def ledger(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Suppliers',
        'page_title': 'Supplier Ledger',
    })

