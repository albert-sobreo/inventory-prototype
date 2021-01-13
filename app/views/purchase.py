from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Purchase_Item, Warehouse, Product, User, Purchase_Order, Vendor
from datetime import date as now
import sweetify
import json
from time import sleep

def inView(request):
    if request.session.is_empty():
        return redirect('/login/')
    try:
        po = Purchase_Order.objects.latest('pk')

        listed_ref_id = po.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            new_ref_id = 'PO-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))
        else:
            new_ref_id = 'PO-{}-{}-0001'.format(listed_date[0], listed_date[1])

    except:
        listed_date = str(now.today()).split('-')
        new_ref_id = 'PO-{}-{}-0001'.format(listed_date[0], listed_date[1])

    context = {
        'items': Product.objects.all().order_by('name'),
        'warehouses': Warehouse.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        'new_ref_id': new_ref_id,
        'vendors': Vendor.objects.all(),
    }
    return render(request, 'purchase-order.html', context)

def getItemRemaining(request):
    data = json.loads(request.body)
    item = Product.objects.get(pk=data['code'])

    return JsonResponse({
        'remaining': item.quantity, 
        'warehouse': {
            'pk': item.warehouse.pk, 
            'name': item.warehouse.name
            },
        'cost_per_item': item.cost_per_item
        })

def purchaseProcess(request):
    data = json.loads(request.body)
    
    ref_id = data['ref_id']
    date = data['date']
    vendor = data['vendor']
    lines = data['lines']
    total_amount_due = data['total_amount_due']

    myUsername = request.session.get('username')

    if vendor == '':
        sweetify.sweetalert(request, icon='error', title="Error", text='Vendor is empty', persistent="Dismiss")
        return JsonResponse(0, safe=False)

    if Purchase_Order.objects.filter(ref_id=ref_id).exists():
        po = Purchase_Order.objects.latest('pk')

        listed_ref_id = po.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            ref_id = 'PO-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))        

    po = Purchase_Order()

    po.ref_id = ref_id
    po.date = date
    po.vendor = Vendor.objects.get(pk=vendor)
    po.total_amount_due = total_amount_due
    po.approved = False
    po.created_by = User.objects.get(login__username=myUsername)

    po.save()
    
    for line in lines:
        pi = Purchase_Item()

        pi.product = Product.objects.get(pk=int(line['code']))
        pi.purchase_order = po
        pi.remaining = int(line['remaining'])
        pi.purchase_quantity = int(line['quantity'])
        pi.cost_per_item = float(line['cost_per_item'])
        pi.total_cost = float(line['total_cost'])

        pi.save()
        sweetify.sweetalert(request, icon='success', title='Success!', persistent='Dismiss')

    return JsonResponse(0, safe=0)