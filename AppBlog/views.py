from django.shortcuts import render
from AppBlog.models import Post
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "\AppBlog\templates\AppBlog\blog.html")

def post(request):
    return HttpResponse("estas en POST")