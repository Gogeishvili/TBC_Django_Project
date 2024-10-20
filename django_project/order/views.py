from django.shortcuts import render
from django.http import HttpResponse

def order_main_page(request):
    return HttpResponse("Order main page")

