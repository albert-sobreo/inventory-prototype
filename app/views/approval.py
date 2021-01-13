from typing import Text
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
import sweetify
from app.models import Product, User, Purchase_Order, Sales_Order
import json
from django.db.models import Avg, Max, Min, Sum

def sales_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'sales': Sales_Order.objects.filter(approved=False),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'sales_not.html', context)

def sales_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'sales': Sales_Order.objects.filter(approved=True),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'sales_approved.html', context)

def purchase_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Purchase_Order.objects.filter(approved=False),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_not.html', context)

def purchase_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'purchases': Purchase_Order.objects.filter(approved=True),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase_approved.html', context)

def getPurchaseModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    object = Purchase_Order.objects.get(pk=pk)

    items = []

    for element in object.purchase_item_set.all():
        items.append({
            'code': element.product.code, 
            'name': element.product.name, 
            'quantity': element.purchase_quantity, 
            'remaining':element.remaining,
            'cost_per_item': element.cost_per_item,
            'total_cost': element.total_cost
        })

    context = {
        'ref_id': object.ref_id,
        'vendor': object.vendor.name,
        'pk': object.pk,
        'items': items
    }
    return JsonResponse(context)

def getSalesModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    sales = Sales_Order.objects.get(pk=pk)

    items = []

    for element in sales.sales_item_set.all():
        items.append({
            'code': element.product.code,
            'name': element.product.name,
            'quantity': element.sales_quantity,
            'remaining': element.remaining,
            'cost_per_item': element.cost_per_item,
            'total_cost': element.total_cost
        })

    context = {
        'ref_id': sales.ref_id,
        'customer': sales.customer.name,
        'pk': sales.pk,
        'items': items
    }
    return JsonResponse(context)

def approvePurchase(request):
    data = json.loads(request.body)

    pk = int(data['pk'])

    purchase = Purchase_Order.objects.get(pk=pk)

    for element in purchase.purchase_item_set.all():
        element.product.quantity += element.purchase_quantity
        element.product.save()

    purchase.approved = True

    purchase.save()

    return JsonResponse(0, safe=0)

def approveSales(request):
    data = json.loads(request.body)

    pk = int(data['pk'])

    sales = Sales_Order.objects.get(pk=pk)

    for element in sales.sales_item_set.all():
        itemize = sales.sales_item_set.filter(product__pk=element.product.pk)
        if itemize.count() > 1:
            total_quantity =itemize.aggregate(total=Sum('sales_quantity'))
            remaining = itemize.aggregate(max=Max('remaining'))

            if total_quantity['total'] > remaining['max']:
                sweetify.sweetalert(request, icon='error', title='Error', html="You are selling <b>" + str(total_quantity['total']) + "</b> {}. You only have: <b>".format(element.product.name) + str(remaining['max']) + "</b>.", persistent='Dismiss')
                return JsonResponse(0, safe=0)

    for element in sales.sales_item_set.all():
        if element.product.quantity < element.sales_quantity:
            sweetify.sweetalert(request, icon='error', title='Error', text="{} has {} items. You are selling {} items.".format(element.product.name, element.product.quantity, element.sales_quantity), persistent='Dismiss')
            return JsonResponse(0, safe=0)
    
    for element in sales.sales_item_set.all():
        element.product.quantity -= element.sales_quantity
        element.product.save()

    sales.approved = True
    sales.save()

    return JsonResponse(0, safe=0)