#from django.views.generic import path
from django.urls import path

from .views import HomePage,Posts,Post

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('posts/',Posts.as_view(),name = 'posts'),
    path('posts/<int:pk>/',Post.as_view(),name= 'post')
]
