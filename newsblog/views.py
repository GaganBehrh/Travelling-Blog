from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model=Post
    querset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'
    paginate_by=6

# Create your views here.
