from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Order index page")

def about(request):
    return HttpResponse("Order about page")