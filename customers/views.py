from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def add_customer(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Customers',
        'page_title': 'Add Customer',
    })

@login_required
def ledger(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Customers',
        'page_title': 'Customer Ledger',
    })

@login_required
def payment_history(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Customers',
        'page_title': 'Payment History',
    })

