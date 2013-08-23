from blog.models import Post
from django.shortcuts import render
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts' : posts})

