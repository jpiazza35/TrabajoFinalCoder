from django.urls import path 
from AppBlog import views



urlpatterns = [
    path('', views.Inicio),
    path('blogs/',views.Post),
    path('about/', views.About)
    
]
