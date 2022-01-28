from django.urls import path 
from AppBlog import views



urlpatterns = [
    path('', views.post, name='Post'),
    path('showpost/<id>',views.showPost, name="ShowPost"),
    path('about/', views.About, name="About"),
    path("comment/<id>", views.comment, name="Comment"),
    path("newpost/", views.newPost, name="NewPost"),
    path('gallery/', views.gallery, name="Gallery"),
    path('contact/', views.contactus, name="Contact"),
    

    
]
