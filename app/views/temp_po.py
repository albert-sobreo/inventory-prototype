from django.shortcuts import redirect, render, HttpResponse

def po(request):
    return render(request, 'temp_purchase_order.html')