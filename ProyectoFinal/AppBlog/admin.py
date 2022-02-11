from django.contrib import admin
from .models import *


#we can customize the way data is displayed in the administration panel according to our convenience
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email','created_on','status')
    list_filter = ("status",'created_on')
    search_fields = ['name', 'email','content']
    



# Register your models here.
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(User)