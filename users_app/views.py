from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def roles_permissions(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Users',
        'page_title': 'Roles & Permissions',
    })

@login_required
def staff_management(request):
    return render(request, 'module_placeholder.html', {
        'module_title': 'Users',
        'page_title': 'Staff Management',
    })

