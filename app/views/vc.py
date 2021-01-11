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
    owner_first_name = request.GET['owner_first_name']
    owner_last_name = request.GET['owner_last_name']
    address = request.GET['address']
    landline = request.GET['landline']
    email = request.GET['email']
    mobile = request.GET['mobile']
    bank = request.GET['bank']
    bank_number = request.GET['bank_number']

    vendor = Vendor()

    vendor.name = ( owner_first_name + " " + owner_last_name)
    vendor.address = address
    vendor.landline = landline
    vendor.email = email
    vendor.mobile = mobile
    vendor.bank = bank
    vendor.bank_number = bank_number

    try:
        vendor.save()
        sweetify.sweetalert(request, icon='success', title='Added Vendor Successfully', text='{} {} successfully added'.format(vendor.name), persistent='Dismiss')
    except:
        sweetify.sweetalert(request, icon='error', title='Something went wrong', persistent='Dismiss')


    return redirect('/vendor/')

def getVendorModalData(request):
    data = json.loads(request.body)
    pk = int(data['pk'])

    vendor = Vendor.objects.get(pk=pk)

    items = []

    for element in vendor.purchase_order_set.all():
        items.append({
            'code': element.ref_id, 
            'date': element.date
        })
    
    context = {
        'name': vendor.name,
        'address' : vendor.address,
        'landline' : vendor.landline,
        'email' : vendor.email,
        'mobile' : vendor.mobile,
        'bank' : vendor.bank,
        'bank_number' : vendor.bank_number,
        'items': items
    }

    return JsonResponse(context)

# Functions for Customers
def customers_save_process(request):
    if request.session.is_empty():
        return redirect('/login/')
    owner_first_name = request.GET['owner_first_name']
    owner_last_name = request.GET['owner_last_name']
    address = request.GET['address']
    landline = request.GET['tele']
    email = request.GET['email']
    mobile = request.GET['num']
    bank = request.GET['bank']
    bank_number = request.GET['account_num']

    customer = Customer()

    customer.name = ( owner_first_name + " " + owner_last_name)
    customer.address = address
    customer.landline = landline
    customer.email = email
    customer.mobile = mobile
    customer.bank = bank
    customer.bank_number = bank_number

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
    
    for element in customer.sales_order_set.all():
        items.append({
            'code': element.ref_id,
            'date': element.date
        })
    
    context = {
        'name': customer.name,
        'address' : customer.address,
        'landline' : customer.landline,
        'email' : customer.email,
        'mobile' : customer.mobile,
        'bank' : customer.bank,
        'bank_number' : customer.bank_number,
        'items': items
    }

    return JsonResponse(context)