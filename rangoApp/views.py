from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango Says Hello World , go to <a href='rangoApp/about'>about</a>")

def about(request):
    return HttpResponse("Rango says : here is the about page! go to <a href='http://localhost:8000/rangoApp'>index</a>" )
