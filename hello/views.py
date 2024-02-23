from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'hello/index.html')

def muskan(request):
    return HttpResponse("Hello,Muskan!")

def david(request):
    return HttpResponse("Hello,David!")

def greet(request,name):
    return HttpResponse(f"Hello,{name.capitalize()}!")   
