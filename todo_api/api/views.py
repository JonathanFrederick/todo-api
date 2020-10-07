from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


# Create your views here.
def home_page(request):
    return render(request, "api/index.html")


@api_view(['POST'])
def register(request):
    User.objects.create_user(
        request.POST['username'],
        request.POST['email'],
        request.POST['password']
    )
    return HttpResponse("", status=201)
