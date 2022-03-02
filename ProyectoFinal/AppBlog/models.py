from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.utils import timezone

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username



class Tag(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
#we created a tuple to determine the status of a blog


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    options = (
    ('draft', "Draft"),
    ('published', "Published"),
)


    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, default=1 )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, null=False, unique=True) ##Esta palabra define la parte final de la URL que identifica una página dentro de un sitio web.
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    content= models.TextField()
    status = models.CharField(max_length=50,choices=options, default='draft')
    image = models.ImageField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    objects = models.Manager() ##to see all objects from db
    postobjects = PostObjects() ## custom way to find just objects that are published.
    
    ## esto va en la vista comments = Comment.objects.filter(post__id = id)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title


'''
The Meta class inside the model contains metadata. 
We tell Django to sort results in the created_on field in descending order by default when we query the database.
We specify descending order using the negative prefix. By doing so, posts published recently will appear first.

The __str__() method is the default human-readable representation of the object. Django will use it in many places, such as the administration site.
'''

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50) #name of the person that make the comment
    email = models.EmailField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("created_on",)
        
        def __str__(self):
            return f"comment by : {self.name}"


class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user
