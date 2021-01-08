from django.shortcuts import render, redirect
from app.models import User, Purchase_Order, Sales_Order

def delivery_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Purchase_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'delivery_not.html', context)

def delivery_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Purchase_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'delivery_approved.html', context)

def warehouse_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Sales_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'warehouse_not.html', context)

def warehouse_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Sales_Order.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'warehouse_approved.html', context)