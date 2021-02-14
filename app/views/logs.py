from django.shortcuts import render, redirect
from app.models import User, Purchase_Order, Sales_Order, Transfer, Spoilage

def purchaseLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'me': User.objects.select_related().get(username=request.session.get('username')),
    }
    return render(request, 'logs_purchase.html', context)

def salesLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'me': User.objects.select_related().get(username=request.session.get('username')),
    }
    return render(request, 'logs_sales.html', context)

def transferLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'me': User.objects.select_related().get(username=request.session.get('username')),
    }
    return render(request, 'logs_transfer.html', context)

def spoilageLogsView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'me': User.objects.select_related().get(username=request.session.get('username')),
    }
    return render(request, 'logs_spoilage.html', context)
    