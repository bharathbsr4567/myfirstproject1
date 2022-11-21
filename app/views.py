from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Bharath(request):
    return HttpResponse('<marquee>first</marquee>')



def Naveen(request):
    return HttpResponse('<h1>Second</h1>')

def first(request):
    return HttpResponse('<marquee><h2>hie good morning</h2></marquee>')

def second(request):
    return HttpResponse('<marquee><h1>fourth</h1></marquee>')