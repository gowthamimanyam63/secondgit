from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('this is my first view')
def second(request):
    return HttpResponse('<h1><marquee>We are groot</marquee></h1>')