from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Store index page")

def about(request):
    return HttpResponse("Store about page")
