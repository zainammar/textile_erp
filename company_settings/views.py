from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def company_info(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Company Settings',
        'page_title': 'Company Information',
    })

@login_required
def invoice_settings(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Company Settings',
        'page_title': 'Invoice Settings',
    })

@login_required
def tax(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Company Settings',
        'page_title': 'Tax',
    })

@login_required
def currency(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Company Settings',
        'page_title': 'Currency',
    })

