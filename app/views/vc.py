from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Vendor, Customer, User, Purchase_Order, Sales_Order
import sweetify, json

def vendors_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'vendors': Vendor.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        
    }
    return render(request, 'vendors.html', context)

def customers_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'customers': Customer.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        
    }
    return render(request, 'customers.html', context)

# Functions for Vendors
def vendors_save_process(request):
    if request.session.is_empty():
        return redirect('/login/')
    name = request.GET['name']
    address = request.GET['address']
    tele = request.GET['tele']
    email = request.GET['email']
    num = request.GET['num']
    bank = request.GET['bank']
    account_num = request.GET['account_num']

    vendor = Vendor()

    vendor.name = name
    vendor.address = address
    vendor.tele = tele
    vendor.email = email
    vendor.num = num
    vendor.bank = bank
    vendor.account_num = account_num

    try:
        vendor.save()
        sweetify.sweetalert(request, icon='success', title='Added Vendor Successfully', text='{} {} successfully added'.format(vendor.name), persistent='Dismiss')
    except:
        sweetify.sweetalert(request, icon='error', title='Something went wrong', persistent='Dismiss')


    return redirect('vendor/')

def getVendorModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    vendor = Vendor.objects.get(pk=pk)

    items = []

    for element in vendor.purchase_order_set.all().purchase_item_set.all():
        items.append({
            'code': element.product.code, 
            'date': element.product.date
        })
    
    for element in vendor.sales_order_set.all().sales_item_set.all():
        items.append({
            'code': element.product.code,
            'date': element.product.date
        })
    
    context = {
        'name': vendor.name,
        'address' : vendor.address,
        'tele' : vendor.tele,
        'email' : vendor.email,
        'num' : vendor.num,
        'bank' : vendor.bank,
        'account_num' : vendor.account_num,
        'items': items
    }

    return JsonResponse(context)

# Functions for Customers
def customer_save_process(request):
    if request.session.is_empty():
        return redirect('/login/')
    name = request.GET['name']
    address = request.GET['address']
    tele = request.GET['tele']
    email = request.GET['email']
    num = request.GET['num']
    bank = request.GET['bank']
    account_num = request.GET['account_num']

    customer = Customer()

    customer.name = name
    customer.address = address
    customer.tele = tele
    customer.email = email
    customer.num = num
    customer.bank = bank
    customer.account_num = account_num

    try:
        customer.save()
        sweetify.sweetalert(request, icon='success', title='Added Customer Successfully', text='{} {} successfully added'.format(customer.name), persistent='Dismiss')
    except:
        sweetify.sweetalert(request, icon='error', title='Something went wrong', persistent='Dismiss')


    return redirect('customer/')

def getCustomerModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    customer = Customer.objects.get(pk=pk)

    items = []

    for element in customer.purchase_order_set.all().purchase_item_set.all():
        items.append({
            'code': element.product.code, 
            'date': element.product.date
        })
    
    for element in customer.sales_order_set.all().sales_item_set.all():
        items.append({
            'code': element.product.code,
            'date': element.product.date
        })
    
    context = {
        'name': customer.name,
        'address' : customer.address,
        'tele' : customer.tele,
        'email' : customer.email,
        'num' : customer.num,
        'bank' : customer.bank,
        'account_num' : customer.account_num,
        'items': items
    }

    return JsonResponse(context)