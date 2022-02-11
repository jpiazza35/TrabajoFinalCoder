'''
from django import forms
from django.forms import widgets
from AppBlog.models import User,Post


class NewPost(forms.Form):
    fields = ['title', 'slug','author', 'content', 'status', 'image']
    
    


class NewComment(forms.Form):
    content = forms.CharField()
    post = forms.Select(Post)
    user = forms.Select(User)
    created_on = forms.DateTimeField(auto_now_add=True)


'''
