from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest

# Create your views here.
def home_page(request):
    return render(request, "api/index.html")

def register(request):
    return HttpRequest("")