from django.http import HttpResponse
from django.shortcuts import render

def list_customers(request):
    return render(request, "customers/customers.html")