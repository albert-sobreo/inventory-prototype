from django.shortcuts import render, redirect
from app.models import Warehouse, Product, User
import sweetify


# Create your views here.
# functions for Warehouse

def inventory_page(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'items': Product.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
        'warehouses': Warehouse.objects.all()
    }
    return render(request, 'inventory.html', context)

def warehouse_save_process(request):
    if request.session.is_empty():
        return redirect('/login/')
    name = request.GET['name']
    address = request.GET['address']

    warehouse = Warehouse()

    warehouse.name = name
    warehouse.address = address
    try:
        warehouse.save()
        sweetify.sweetalert(request, icon='success', title='Added Warehouse Successfully!', persistent='Dismiss')
    except:
        sweetify.sweetalert(request, icon='error', title='YOU DID IT', text="YOU FUCKED IT UP", persistent='BRUH')

    return redirect('/')

def warehouse_list(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'warehouses': Warehouse.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username'))
    }
    return render(request, 'warehouse.html', context)

#def warehouse_delete(request, id):
#    Warehouse.objects.filter(id=id).delete{
#        return redirect('/warehouse_list')
#    }


def warehouse_edit(request, id):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'app': Warehouse.objects.get(id=id)
    }
    return render(request, 'warehouseedit.html', context)

def warehouse_edit_save(request, id):
    if request.session.is_empty():
        return redirect('/login/')
    warehouse = Warehouse.objects.get(id=id)
    warehouse.name=request.POST['name']
    warehouse.address=request.POST['address']

    warehouse.save()
    return redirect('warehouse_list')

# functions for Inventory list
def inventory_save_process(request):
    if request.session.is_empty():
        return redirect('/login/')
    code = request.GET['code']
    name = request.GET['name']
    description = request.GET['description']
    quantity = int(request.GET['quantity'])

    warehouse_pk = int(request.GET['warehouse'])

    product = Product()

    product.code = code
    product.name = name
    product.description = description
    product.quantity = quantity
    product.warehouse = Warehouse.objects.get(pk=warehouse_pk)

    try:
        product.save()
        sweetify.sweetalert(request, icon='success', title='Added Product Successfully', text='{} {} successfully added'.format(product.quantity, product.name), persistent='Dismiss')
    except:
        sweetify.sweetalert(request, icon='error', title='Something went wrong', persistent='Dismiss')


    return redirect('/inventory-page')

def inventory_delete(request, id):
    if request.session.is_empty():
        return redirect('/login/')
    Product.objects.filter(id=id).delete()
    return redirect('/')
    
def inventory_edit(request, id):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'app': Product.objects.get(id=id), 'Warehouse': Warehouse.objects.all()
    }
    return render(request, 'edit.html', context)

def inventory_edit_save(request, id):
    if request.session.is_empty():
        return redirect('/login/')
    product = Product.objects.get(id=id)
    product.code = request.POST['code']
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.quantity = request.POST['quantity']
    product.turnover = request.POST['turnover']
