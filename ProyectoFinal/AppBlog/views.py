from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Inicio(request):
    return HttpResponse("ESTO ES EL INICIO")

def Blog(request):
    return HttpResponse("this is Blog section")

def About(request):
    return HttpResponse('About section')


#def create_blog(request):
 #   blog = Blog()
