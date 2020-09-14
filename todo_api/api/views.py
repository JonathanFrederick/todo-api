from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_page(request):
    return render(request, "api/index.html")