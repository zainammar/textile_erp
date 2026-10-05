from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def order(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Sales',
        'page_title': 'Sales Order',
    })

@login_required
def invoice(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Sales',
        'page_title': 'Sales Invoice',
    })

@login_required
def delivery_challan(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Sales',
        'page_title': 'Delivery Challan',
    })

@login_required
def return_management(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Sales',
        'page_title': 'Return Management',
    })

