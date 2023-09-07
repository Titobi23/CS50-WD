from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, "hello/index.html")

def titobi(request):
    return HttpResponse("Hello, Titobi!")

def leticia(request):
    return HttpResponse("Hello, Leticia!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })