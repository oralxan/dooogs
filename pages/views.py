from django.views.generic import TemplateView,ListView,DetailView
from .models import Post

class HomePage(TemplateView):
    template_name = 'pages/home.html'
class Posts(ListView):
    model=Post
    template_name = 'pages/posts.html'
    context_object_name = 'posts'
class Post(DetailView):
    model = Post
    template_name = 'pages/detail.html'
    context_object_name = 'post'