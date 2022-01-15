from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio),
    path('post/', views.post),
]