from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import *

# Create your views here.

def post(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request,"AppBlog/inicio.html", {"posts": posts})

def showPost(request, id):
    post = Post.objects.get(id=id)
    tags = Tag.objects.filter(post__id=id)
    return render(request, "AppBlog/show.html", {"post": post, "tags": tags})

def comment(request, id):
    comment= Comment.objects.get(id=id)
    return render(request, "AppBlog/comment.html",{"comment": comment})

def About(request):
    return render(request, 'AppBlog/about.html')


#def create_blog(request):
 #   blog = Blog()
