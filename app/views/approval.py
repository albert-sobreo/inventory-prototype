from django.http.response import JsonResponse
from django.shortcuts import render, redirect
import sweetify
from app.models import Spoilage, Transfer, User, Purchase_Order, Sales_Order
import json
from decimal import Decimal, ROUND_05UP

def sales_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))
    context = {
        'sales': user.branch.sales_order.filter(approved=False),
        'me': user
    }
    return render(request, 'sales_not.html', context)

def sales_approved(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))
    context = {
        'sales': user.branch.sales_order.filter(approved=True),
        'me': user
    }
    return render(request, 'sales_approved.html', context)

def purchase_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')
    
    user = User.objects.get(username=request.session.get('username'))
    context = {
        'purchases': user.branch.purchase_order.filter(approved=False),
        'me': user
    }
    return render(request, 'purchase_not.html', context)

def purchase_approved(request):
    if request.session.is_empty():
        return redirect('/login/')
    
    user = User.objects.get(username=request.session.get('username'))
    context = {
        'purchases': user.branch.purchase_order.filter(approved=True),
        'me': user
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
            'remaining':element.product.quantity,
            'cost_per_item': element.cost_per_item,
            'total_cost': element.total_cost,
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
            'remaining': element.product.quantity,
            'cost_per_item': element.cost_per_item,
            'total_cost': element.total_cost,
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
        element.product.total_cost += element.total_cost
        element.product.save()
        element.product.cost_per_item = (Decimal((element.product.total_cost / element.product.quantity)))
        element.product.save()

    purchase.approved = True

    purchase.save()

    return JsonResponse(0, safe=0)

def approveSales(request):
    data = json.loads(request.body)

    pk = int(data['pk'])

    sales = Sales_Order.objects.get(pk=pk)

    for element in sales.sales_item_set.all():
        if element.product.quantity < element.sales_quantity:
            sweetify.sweetalert(request, icon='error', title='Error', text="{} has {} items. You are selling {} items.".format(element.product.name, element.product.quantity, element.sales_quantity), persistent='Dismiss')
            return JsonResponse(0, safe=0)
    
    for element in sales.sales_item_set.all():
        element.product.quantity -= element.sales_quantity
        element.product.total_cost -= element.total_cost
        element.product.save()

    sales.approved = True
    sales.save()

    return JsonResponse(0, safe=0)

# For Spoilage and Transfer

def transfer_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))
    context = {
        'transfers': user.branch.transfer.filter(approved=False),
        'me': user
    }
    return render(request, 'transfer_not.html', context)

def transfer_approved(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))
    context = {
        'transfers': user.branch.transfer.filter(approved=True),
        'me': user
    }
    return render(request, 'transfer_approved.html', context)

def spoilage_notapproved(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))
    context = {
        'spoils': user.branch.spoilage.filter(approved=False),
        'me': user
    }
    return render(request, 'spoilage_not.html', context)

def spoilage_approved(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))
    context = {
        'spoils': user.branch.spoilage.filter(approved=True),
        'me': user
    }
    return render(request, 'spoilage_approved.html', context)

def getTransferModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    object = Transfer.objects.get(pk=pk)

    items = []

    for element in object.transfer_item_set.all():
        items.append({
            'code': element.product.code,
            'name': element.product.name,
            'quantity': element.transfer_quantity,
            'old_warehouse':element.product.warehouse.name
            })

    context = {
        'ref_id': object.ref_id,
        'new_warehouse': object.warehouse.name,
        'pk': object.pk,
        'items': items
    }
    return JsonResponse(context)

def getSpoilageModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    object = Spoilage.objects.get(pk=pk)

    items = []

    for element in object.spoilage_item_set.all():
        items.append({
            'code': element.product.code,
            'name': element.product.name,
            'quantity': element.spoilage_quantity,
            'remaining':element.product.quantity,
            'reason':element.reason,
            'cost_per_item': element.cost_per_item,
            'total_cost': element.total_cost,
            })

    context = {
        'ref_id': object.ref_id,
        'total_lost': object.total_lost,
        'pk': object.pk,
        'items': items
    }
    return JsonResponse(context)

def approveTransfer(request):
    data = json.loads(request.body)

    pk = int(data['pk'])

    transfer = Transfer.objects.get(pk=pk)

    for element in transfer.transfer_item_set.all():
        element.product.warehouse = transfer.warehouse
        element.product.save()
        

    transfer.approved = True

    transfer.save()

    return JsonResponse(0, safe=0)

def approveSpoilage(request):
    data = json.loads(request.body)

    pk = int(data['pk'])

    spoils = Spoilage.objects.get(pk=pk)

    for element in spoils.spoilage_item_set.all():
        element.product.quantity -= element.spoilage_quantity
        element.product.total_cost -= element.total_cost
        element.product.save()

        
        
    spoils.approved = True
    spoils.save()

    return JsonResponse(0, safe=0)