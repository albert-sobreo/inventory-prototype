from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Customer, Sales_Item, Sales_Order, Spoilage, Transfer, Transfer_Item, Warehouse, Product, User
import sweetify
from datetime import date as now
import json

def transferView(request):
    if request.session.is_empty():
        return redirect('/login/')
    user = User.objects.get(username=request.session.get('username'))
    try:
        tr = user.branch.transfer.latest('pk')

        listed_ref_id = tr.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            new_ref_id = 'T-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))
        else:
            new_ref_id = 'T-{}-{}-0001'.format(listed_date[0], listed_date[1])

    except:
        listed_date = str(now.today()).split('-')
        new_ref_id = 'T-{}-{}-0001'.format(listed_date[0], listed_date[1])

    context = {
        'me': User.objects.select_related().get(username=request.session.get('username')),
        'new_ref_id': new_ref_id,
    }
    return render(request, 'transfer.html', context)

def transferProcess(request):
    data = json.loads(request.body)

    ref_id = data['ref_id']
    date = data['date']
    new_warehouse = data['new_warehouse']
    lines = data['lines']

    myUsername = request.session.get('username')
    user = User.objects.get(username=myUsername)

    if user.branch.transfer.filter(ref_id=ref_id).exists():
        tr = user.branch.transfer.latest('pk')

        listed_ref_id = tr.ref_id.split('-')
        listed_date = str(now.today()).split('-')

        current_code = int(listed_ref_id[3])

        if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
            current_code += 1
            ref_id = 'T-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))

    tr = Transfer()

    tr.ref_id = ref_id
    tr.date = date
    tr.warehouse = Warehouse.objects.get(pk=new_warehouse)
    tr.approved = False
    tr.created_by = User.objects.get(username=myUsername)
    tr.save()

    user.branch.transfer.add(tr)

    for line in lines:
        ti = Transfer_Item()
  
        ti.product = Product.objects.get(pk=int(line['code']))
        ti.transfer = tr
        ti.remaining = int(line['remaining'])
        ti.transfer_quantity = int(line['quantity'])

        ti.save()
        sweetify.sweetalert(request, icon='success', title='Success!', persistent='Dismiss')

    return JsonResponse(0, safe=0)