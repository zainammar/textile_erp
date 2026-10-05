from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def income(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Accounts',
        'page_title': 'Income',
    })

@login_required
def expense(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Accounts',
        'page_title': 'Expense',
    })

@login_required
def cash_book(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Accounts',
        'page_title': 'Cash Book',
    })

@login_required
def bank_book(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Accounts',
        'page_title': 'Bank Book',
    })

@login_required
def customer_ledger(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Accounts',
        'page_title': 'Customer Ledger',
    })

@login_required
def supplier_ledger(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Accounts',
        'page_title': 'Supplier Ledger',
    })

