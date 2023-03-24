from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Articles

def front_page(request):

    posts = Articles.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'home.html', context)


def single(request, slug):
    post = get_object_or_404(Articles, slug=slug)

    context = {
        'post': post,
    }


    return render(request, 'single.html', context)

