from django.shortcuts import redirect, render, HttpResponse
from app.models import Purchase_Order
from datetime import date

def po(request):
    po = Purchase_Order.objects.latest('pk')

    listed_ref_id = po.ref_id.split('-')
    listed_date = str(date.today()).split('-')

    current_code = int(listed_ref_id[3])

    if listed_ref_id[1] == listed_date[0] and listed_ref_id[2] == listed_date[1]:
        current_code += 1
        new_ref_id = 'PO-{}-{}-{}'.format(listed_date[0], listed_date[1], str(current_code).zfill(4))
    else:
        new_ref_id = 'PO-{}-{}-0001'.format(listed_date[0], listed_date[1])


    context = {
        'po': po,
        'new_ref_id': new_ref_id
    }
    return render(request, 'temp_purchase_order.html', context)

def poProcess(request):
    ref_id = request.GET['ref_id']
    date = request.GET['date']

    po = Purchase_Order()

    po.ref_id = ref_id
    po.date = date
    po.approved = False

    po.save()

    return redirect('/temp-po')