from django.shortcuts import render, redirect
from app.models import User, Purchase_Order, Sales_Order, Transfer, Spoilage

def purchase_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Purchase_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_log.html', context)

def sales_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'sales': Sales_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'sales_log.html', context)

def transfer_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'transfers': Transfer.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'transfer_log.html', context)

def spoilage_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'spoils': Spoilage.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'spoilage_logs.html', context)
    