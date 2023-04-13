from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment


def home(request):
    return render(request, 'home.html')


def blog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comments = blog.comment_set.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            blog = blog,
            body = request.POST.get('body'),
        )
        return redirect('blog:blog_detail', blog.id)

    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blog_detail.html', context)


def delete_comment(request, pk, id):
    blog = get_object_or_404(Blog, id=pk)
    if pk:
        comment = Comment.objects.get(id=id)
        comment.delete()

        return redirect('blog:blog_detail', blog.pk)

    return render(request, 'blog_detail.html')
