from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Customer, Sales_Item, Sales_Order, Spoilage, Spoilage_Item, Transfer, Transfer_Item, Warehouse, Product, User
import sweetify
from datetime import date as now
import json
from decimal import Decimal

def spoilageView(request):
    if request.session.is_empty():
        return redirect('/login/')
    
    user = User.objects.get(username=request.session.get('username'))

    try:
        tr = user.branch.spoilage.latest('pk')

        listed_ref_id = tr.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            new_ref_id = 'SP-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))
        else:
            new_ref_id = 'SP-{}-{}-0001'.format(listed_date[0], listed_date[1])

    except:
        listed_date = str(now.today()).split('-')
        new_ref_id = 'SP-{}-{}-0001'.format(listed_date[0], listed_date[1])

    context = {
        'me': user,
        'new_ref_id': new_ref_id,
    }
    return render(request, 'spoilage.html', context)

def spoilageProcess(request):
    data = json.loads(request.body)

    ref_id = data['ref_id']
    date = data['date']
    lines = data['lines']
    total_lost = data['total_lost']
    
    myUsername = request.session.get('username')
    user = User.objects.get(username=request.session.get('username'))

    if user.branch.spoilage.filter(ref_id=ref_id).exists():
        sp = user.branch.spoilage.latest('pk')

        listed_ref_id = sp.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            ref_id = 'SP-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))

    sp = Spoilage()

    sp.ref_id = ref_id
    sp.date = date
    sp.total_lost = total_lost
    sp.approved = False
    sp.created_by = User.objects.get(username=myUsername)
    sp.save()

    user.branch.spoilage.add(sp)

    for line in lines:
        si = Spoilage_Item()

        si.product = Product.objects.get(pk=int(line['code']))
        si.spoilage = sp
        si.remaining = int(line['remaining'])
        si.spoilage_quantity = int(line['quantity'])
        si.reason = line['reason']
        si.cost_per_item = float(line['cost_per_item'])
        si.total_cost = float(line['total_cost'])

        si.save()
        sweetify.sweetalert(request, icon='success', title='Success!', persistent='Dismiss')

    return JsonResponse(0, safe=0)