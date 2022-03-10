from django.urls import path 
from AppBlog.views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView,
    about
)




urlpatterns = [
    path('', PostListView.as_view(), name="list_posts"),
    path('about/',about, name="about"),
    path('showpost/<slug>/',PostDetailView.as_view(), name="detail_post"),
    path("newpost/", PostCreateView.as_view(), name="create_post"),
    path("<slug>/update/", PostUpdateView.as_view(), name="update_post"),
    path("<slug>/delete/", PostDeleteView.as_view(), name="delete_post"),

    #path('gallery/', views.gallery, name="Gallery"),
    #path('contact/', views.contacts, name="Contact"),
    #path('about/', views.About, name="About"),
    

    
]
