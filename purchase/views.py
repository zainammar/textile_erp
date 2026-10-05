from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def orders(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Purchase',
        'page_title': 'Purchase Orders',
    })

@login_required
def receive_goods(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Purchase',
        'page_title': 'Receive Goods',
    })

@login_required
def invoice(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Purchase',
        'page_title': 'Purchase Invoice',
    })

