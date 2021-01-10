from django.shortcuts import render, redirect
from app.models import User, Purchase_Order, Sales_Order, Transfer, Spoilage

def purchaseLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Purchase_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'logs_purchase.html', context)

def salesLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'sales': Sales_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'logs_sales.html', context)

def transferLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'transfers': Transfer.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'logs_transfer.html', context)

def spoilageLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'spoils': Spoilage.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'logs_spoilage.html', context)
    