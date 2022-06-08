from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'backand/index.html')


def about(request):
    return render(request, 'backand/about.html')


def signin(request):
    return render(request, 'backand/signin_signup.html')