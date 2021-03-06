from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Customer, Sales_Item, Sales_Order, Warehouse, Product, User
import sweetify
from datetime import date as now
import json
from time import sleep

def outView(request):
    if request.session.is_empty():
        return redirect('/login/')

    user = User.objects.get(username=request.session.get('username'))

    try:
        so = user.branch.sales_order.latest('pk')

        listed_ref_id = so.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            new_ref_id = 'SO-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))
        else:
            new_ref_id = 'SO-{}-{}-0001'.format(listed_date[0], listed_date[1])

    except:
        listed_date = str(now.today()).split('-')
        new_ref_id = 'SO-{}-{}-0001'.format(listed_date[0], listed_date[1])

    
    context = {
        'me': user,
        'new_ref_id': new_ref_id,
    }
    return render(request, 'sales-order.html', context)


def salesProcess(request):
    data = json.loads(request.body)

    ref_id = data['ref_id']
    date = data['date']
    customer = data['customer']
    lines = data['lines']
    total_amount_due = data['total_amount_due']

    myUsername = request.session.get('username')
    user = User.objects.get(username=myUsername)

    if customer == '':
        sweetify.sweetalert(request, icon='error', title='Error', text='Customer is empty', persistent="Dismiss")
        return JsonResponse(0, safe=False)

    if user.branch.sales_order.filter(ref_id=ref_id).exists():
        so = user.branch.sales_order.latest('pk')

        listed_ref_id = so.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            new_ref_id = 'SO-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))

    so = Sales_Order()

    so.ref_id = ref_id
    so.date = date
    so.customer = Customer.objects.get(pk=customer)
    so.total_amount_due = total_amount_due
    so.approved = False
    so.created_by = User.objects.get(username=myUsername)

    so.save()
    user.branch.sales_order.add(so)

    for line in lines:
        si = Sales_Item()

        si.product = Product.objects.get(pk=int(line['code']))
        si.sales_order = so
        si.remaining = int(line['remaining'])
        si.sales_quantity = int(line['quantity'])
        si.cost_per_item = float(line['cost_per_item'])
        si.total_cost = float(line['total_cost'])

        si.save()
        sweetify.sweetalert(request, icon='success', title='Success!', persistent='Dismiss')

    return JsonResponse(0, safe=0)