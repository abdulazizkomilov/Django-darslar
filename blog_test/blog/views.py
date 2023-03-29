from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Articles
from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')
    posts = Articles.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))

    context = {
        'query': query,
        'posts': posts,
    }

    return render(request, 'search.html', context)

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

