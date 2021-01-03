from django.shortcuts import render, redirect
from app.models import Warehouse, Product 


# Create your views here.
# functions for Warehouse
def inventory_page(request):
    context = {
        'Warehouse': Warehouse.objects.all()
    }
    return render(request, 'inventory_page.html', context)

def warehouse_save_process(request):
    name = request.POST['name']
    address = request.POST['address']

    warehouse = Warehouse()

    warehouse.name = name
    warehouse.address = address

    warehouse.save()
    
    return redirect('/')

def warehouse_list(request):
    context = {
        'app': Warehouse.objects.all()  
    }
    return render(request, 'warehouselist.html', context)

def warehouse_delete(request, id):
    Warehouse.objects.filter(id=id).delete{
        return redirect('/warehouse_list')
    }


def warehouse_edit(request, id):
    context = {
        'app': Warehouse.objects.get(id=id)
    }
    return render(request, 'warehouseedit.html', context)

def warehouse_edit_save(request, id):
    warehouse = Warehouse.objects.get(id=id)
    warehouse.name=request.POST['name']
    warehouse.address=request.POST['address']

    warehouse.save()
    return redirect('warehouse_list')

# functions for Inventory list
def inventory_save_process(request):
    code = request.POST['code']
    name = request.POST['name']
    description = request.POST['description']
    quantity = request.POST['quantity']
    turnover = request.POST['turnover']

    product = Product()

    product.code = code
    product.name = name
    product.description = description
    product.quantity = quantity
    product.turnover = turnover

    product.save()
    return redirect('/')

def inventory_delete(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('/')
    
def inventory_edit(request, id):
    context = {
        'app': Product.objects.get(id=id), 'Warehouse': Warehouse.objects.all()
    }
    return render(request, 'edit.html', context)

def inventory_edit_save(request, id):
    product = Product.objects.get(id=id)
    product.code = request.POST['code']
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.quantity = request.POST['quantity']
    product.turnover = request.POST['turnover']
