from django import http
from django.shortcuts import render, redirect, HttpResponse
from app.models import Spoilage, Branch, User

def topLevelHome(request):
    if request.session.is_empty():
        return redirect('/login/')
    print(request.session.get('top-level'))
    if not request.session.get('top-level'):
        return HttpResponse('access denied')

    context = {
        "me": User.objects.get(username=request.session.get('username')),
    }
    return render(request, 'tlHome.html', context)

def topLevelBranchInvnetory(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchInventory.html', context)

def topLevelBranchWarehouse(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }

    return render(request, 'tlBranchWarehouse.html', context)

def topLevelCustomers(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlCustomers.html', context)

def topLevelSuppliers(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlSuppliers.html', context)

def topLevelPurchase(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlPurchase.html', context)

def topLevelSales(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlSales.html', context)

def topLevelTransfers(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlTransfers.html', context)

def topLevelSpoilage(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlSpoilage.html', context)

def topLevelApprovals(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlApprovals.html', context)
