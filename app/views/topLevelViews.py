from django import http
from django.shortcuts import render, redirect, HttpResponse
from app.models import Spoilage, Branch, User, Customer, Vendor

def topLevelHome(request):
    if request.session.is_empty():
        if not request.session.get('top-level'):
            return HttpResponse('access denied')
        return redirect('/login/')

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

def topLevelBranchLogsPurchase(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchLogsPurchase.html', context)

def topLevelBranchLogsSales(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchLogsSales.html', context)

def topLevelBranchLogsTransfers(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchLogsTransfers.html', context)

def topLevelBranchLogsSpoilage(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchLogsSpoilage.html', context)

def topLevelBranchCostOfGoodSold(request, pk_branch):
    branch = Branch.objects.get(pk=pk_branch)
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlBranchCostOfGoodSold.html', context)


def topLevelEmployees(request):
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
    }
    return render(request, 'tlEmployees.html', context)

def topLevelCustomers(request):
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        'customers': Customer.objects.all(),
    }
    return render(request, 'tlCustomers.html', context)

def topLevelSuppliers(request):
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        'suppliers': Vendor.objects.all()
    }
    return render(request, 'tlSuppliers.html', context)

def topLevelPurchase(request):
    branch = Branch.objects.all()
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlPurchase.html', context)

def topLevelSales(request):
    branch = Branch.objects.all()
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlSales.html', context)

def topLevelTransfers(request):
    branch = Branch.objects.all()
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlTransfers.html', context)

def topLevelSpoilage(request):
    branch = Branch.objects.all()
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlSpoilage.html', context)

def topLevelApprovals(request):
    branch = Branch.objects.all()
    context = {
        "me": User.objects.get(username=request.session.get('username')),
        'sidebranches': Branch.objects.all(),
        "branch": branch
    }
    return render(request, 'tlApprovals.html', context)
