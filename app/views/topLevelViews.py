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