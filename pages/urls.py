#from django.views.generic import path
from django.urls import path

from .views import HomePage,PostList,PostDetail,PostCreate

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('posts/',PostList.as_view(),name = 'posts'),
    path('posts/<int:pk>/',PostDetail.as_view(),name= 'post'),
    path('posts/create/', PostCreate.as_view(),name='post_create')

]
