from django.shortcuts import render, redirect
from app.models import Warehouse, Product, User
import sweetify

def inView(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'items': Product.objects.all(),
        'me': User.objects.select_related().get(login__username=request.session.get('username')),
    }
    return render(request, 'purchase-order.html', context)