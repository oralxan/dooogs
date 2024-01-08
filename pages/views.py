from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView
)
from .models import Post

class HomePage(TemplateView):
    template_name = 'pages/home.html'
class PostList(ListView):
    model=Post
    template_name = 'pages/posts.html'
    context_object_name = 'post_list'
class PostDetail(DetailView):
    model = Post
    template_name = 'pages/detail.html'
    context_object_name = 'post_datail'

class PostCreate(CreateView):
    model = Post
    template_name = 'pages/create.html'
    content_type = 'post_create'
    fields = ['title','description','image']

