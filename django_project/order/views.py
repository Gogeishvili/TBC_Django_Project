from django.shortcuts import render
from django.http import HttpResponse



def cart(request):
    return render(request,'cart.html',{})

def chackout(request):
    return render(request,'chackout.html',{})