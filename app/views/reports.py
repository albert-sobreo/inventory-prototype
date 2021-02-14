from django.shortcuts import render, redirect
from app.models import Product, User


def costOfGoodSold(request):
    if request.session.is_empty():
        return redirect('/login/')
    context = {
        'me': User.objects.get(username=request.session.get('username')),
    }
    return render(request, 'costofgoodsold.html', context)