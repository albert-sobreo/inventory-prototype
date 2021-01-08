from django.shortcuts import render, redirect
from app.models import Warehouse, Product, User, Vendor, Customer, Purchase_Item, Purchase_Order, Sales_Item, Sales_Order, Transfer, Transfer_Item, Spoilage, Spoilage_Item

def purchase_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'items': Product.objects.all().order_by('name'),
        'warehouses': Warehouse.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        'ref_id': new_ref_id,
        'vendors': Vendor.objects.all(),
    }
    return render(request, 'purchase_log.html', context)

def sales_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'items': Product.objects.all().order_by('name'),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        'new_ref_id': new_ref_id,
        'customers': Customer.objects.all(),
    }
    return render(request, 'sales_log.html', context)

def transfer_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'items': Product.objects.all().order_by('name'),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        'new_ref_id': new_ref_id,
        'customers': Customer.objects.all(),
        'warehouses': Warehouse.objects.all(),
    }
    return render(request, 'transfer_log.html', context)

def spoilage_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    return render(request, 'spoilage_logs.html', context)
    