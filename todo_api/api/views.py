from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from rest_framework.decorators import api_view

# Create your views here.
def home_page(request):
    return render(request, "api/index.html")

@api_view(['POST'])
def register(request):
    return HttpResponse("", status=201)