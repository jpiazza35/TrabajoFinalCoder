from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Inicio(request):
    return HttpResponse("ESTO ES EL INICIO")

def Post(request, post_id):
    
    
    
    return HttpResponse("this is Blog section")

def About(request):
    return HttpResponse('About section')


#def create_blog(request):
 #   blog = Blog()
