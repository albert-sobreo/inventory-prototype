from django.shortcuts import render, redirect
from app.models import Spoilage, Branch

def topLevelHome(request):
    context = {
        'sidebranches': Branch.objects.all()
    }
    return render(request, 'tlHome.html', context)

def topLevelBranchInvnetory(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchInventory.html', context)

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
    return render(request, 'tlSupplies.html', context)

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