from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User

def home(request):

    # all_posts = Post.objects.all() #all post
    all_posts = Post.newmanager.all()

    return render(request, 'home.html', {'posts': all_posts})

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post': post})


def user(request): #ORM
    
    users = User.objects.all()

    return render(request, 'user.html', {'posts': users})


class AddView(CreateView):
    model = Post
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:home')


class EditView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:home')


class Delete(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:home')
    template_name = 'confirm-delete.html'
