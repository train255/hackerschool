from blog.models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts' : posts})


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})
