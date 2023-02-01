from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

def home(request):

    # all_posts = Post.objects.all() #all post
    all_posts = Post.newmanager.all()

    return render(request, 'home.html', {'posts': all_posts})


def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post': post})
