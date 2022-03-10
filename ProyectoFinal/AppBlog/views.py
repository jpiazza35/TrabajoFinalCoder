from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DeleteView,CreateView,UpdateView, DetailView
from .models import Post, Comment, PostView,Like

# Create your views here.
##views de formularios 
##we use views based in classes.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post

def about(request):
    return render(request, 'AppBlog/about.html')




'''
forma mas rebuscada:
def newPost(request):
    if(request.method == 'POST'):
        post_formulario = NewPost(request.POST)
        if(post_formulario.is_valid()):
            information = post_formulario.cleaned_data
            post = Post(title=information['title'], slug =information['slug'], author=information['author'],content=information['content'],status=information['status'], image=information['image'],created_on=information['created_on'], updated_on=information['updated_on'])
            post.save()
            return render(request, "AppBlog/inicio.html") 
    else:
        post_formulario = NewPost() 
        return render(request, "AppBlog/newPost.html", {'form': post_formulario}) ##enviamos el formulario como contexto


##Muestra todos los post
def post(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request,"AppBlog/posts.html", {"posts": posts})

##muestra el post segun id
def showPost(request, id):
    post = Post.objects.get(id=id)
    tags = Tag.objects.filter(post__id=id)
    return render(request, "AppBlog/single.html", {"post": post, "tags": tags})

##aca es donde los users dejan los commentario en cada post
def comment(request, id):
    comment= Comment.objects.get(id=id)
    return render(request, "AppBlog/comment.html",{"comment": comment})

def About(request):
    return render(request, 'AppBlog/about.html')

def gallery(request):
    return render(request, 'AppBlog/gallery.html')

def contacts(request):
    return render(request, 'AppBlog/contact.html')



#def create_blog(request):
 ##   blog = Blog()

'''
