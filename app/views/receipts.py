from django.shortcuts import render, redirect
from app.models import User, Purchase_Order, Sales_Order

def sales_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Sales_Order.objects.filter(approved=False),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'sales_not.html', context)

def sales_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Sales_Order.objects.filter(approved=True),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'sales_approved.html', context)

def purchase_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'sales': Purchase_Order.objects.filter(approved=False),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_not.html', context)

def purchase_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'sales': Purchase_Order.objects.filter(approved=True),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_approved.html', context)