from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def fabric_category(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'Fabric Category',
    })

@login_required
def fabric_quality(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'Fabric Quality',
    })

@login_required
def color(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'Color',
    })

@login_required
def design(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'Design',
    })

@login_required
def gsm(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'GSM',
    })

@login_required
def width(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'Width',
    })

@login_required
def unit(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Products',
        'page_title': 'Unit',
    })

