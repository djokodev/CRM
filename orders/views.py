from django.http import HttpResponse
from django.shortcuts import render

def list_orders(request):
    return render(request, "orders/orders.html")
