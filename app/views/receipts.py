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
<<<<<<< HEAD
        'purchases': Purchase_Order.objects.filter(approved=True),
=======
        'purchases': Sales_Order.objects.filter(approved=True),
>>>>>>> 31f192c6973e2a944eb288799d570518def03fd9
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'sales_approved.html', context)

def purchase_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
<<<<<<< HEAD
        'sales': Sales_Order.objects.filter(approved=False),
=======
        'sales': Purchase_Order.objects.filter(approved=False),
>>>>>>> 31f192c6973e2a944eb288799d570518def03fd9
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_not.html', context)

def purchase_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
<<<<<<< HEAD
        'sales': Sales_Order.objects.filter(approved=True),
=======
        'sales': Purchase_Order.objects.filter(approved=True),
>>>>>>> 31f192c6973e2a944eb288799d570518def03fd9
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_approved.html', context)