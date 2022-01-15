from django.db import models

# Create your models here.
class Post(models.Model):
    nombre = models.CharField(max_length=40)
    texto= models.CharField(max_length=40)
    fecha= models.DateField(auto_now=False, auto_now_add=False)
    # imagen= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
