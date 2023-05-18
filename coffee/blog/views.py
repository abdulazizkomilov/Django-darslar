from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Blog, Comment, User

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #flashmessages
from .forms import MyUserCreationForm, UserForm, BlogForm, BlogCreateForm, CommentForm
from django.contrib.auth.decorators import login_required


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {
        'page': page,
    }
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('blog:home')


def registerPage(request):
    page = 'Sign Up'
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('blog:login')
        else:
            pass

    else:
        form = MyUserCreationForm()

    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'registration/login.html', context)



@login_required(login_url='login')
def updateUser(request, pk):
    page = 'User Update'

    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('blog:account', pk=pk)
        else:
            messages.error(request, 'This username was already used')

    return render(request, 'form.html', {'form': form, 'page': page,})


# -------------------- new ---------------------
def home(request):
    blogs = Blog.objects.all()
    users = User.objects.all()
    commments = Comment.objects.all()

    context = {
        'blogs': blogs,
        'users': users,
        'commments': commments,
    }
    return render(request, 'home.html', context)


def users(request, pk):
    user = User.objects.get(id=pk)

    context = {
        'user': user,
    }
    return render(request, 'components/users.html', context)



def createPost(request):
    page = 'Create Post'
    if request.method == 'POST':
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post =  form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post succesfully created.')
            return redirect('blog:blog')
        else:
            pass

    else:
        form = BlogCreateForm()

    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'form.html', context)




def account(request, pk):
    user = get_object_or_404(User, id=pk)
    blogs = Blog.objects.filter(author=user)

    context = {
        'user': user,
        'blogs': blogs,
    }
    return render(request, 'registration/account.html', context)


def delete_blog(request, pk, id):
    user = get_object_or_404(User, id=id)
    if pk:
        blog = Blog.objects.get(id=pk)
        blog.delete()

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'account.html')



def blog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)


@login_required(login_url='login')
def like_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if pk:
        blog.like.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')


@login_required(login_url='login')
def deslike_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if pk:
        blog.like.remove(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')

@login_required(login_url='login')
def follow_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if pk:
        blog.participants.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')


@login_required(login_url='login')
def unfollow_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if pk:
        blog.participants.remove(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')



@login_required(login_url='login')
def user_follow(request, pk):
    user_p = get_object_or_404(User, id=pk)
    if pk:
        user_p.follower.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')


@login_required(login_url='login')
def user_unfollow(request, pk):
    user_p = get_object_or_404(User, id=pk)
    if pk:
        user_p.follower.remove(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')




@login_required(login_url='login')
def blogUpdate(request, pk):
    page = 'Blog Update'
    blog = get_object_or_404(Blog, id=pk)
    user = request.user
    form = BlogForm(instance=blog)

    if request.user != blog.author:
        return HttpResponse('You are not allowed here')


    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:account', pk=user.id)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'form.html', {'form': form, 'page':page})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comments = blog.comment_set.all()

    #  ----------------------  new  ------------------------
    fav = bool

    if blog.favourites.filter(id=request.user.id).exists():
        fav = True


    comments_count = comments.count()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            body = comment_form.cleaned_data['body']
            try:
                parent = comment_form.cleaned_data['parent']
            except:
                parent=None

        new_comment = Comment(body=body, user=request.user, blog=blog, parent=parent)
        new_comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
        'comments': comments,
        'comments_count': comments_count,
        'fav': fav,
    }
    return render(request, 'blog_detail.html', context)


@login_required
def favourite_list(request):
    new = Blog.objects.filter(favourites=request.user)
    return render(request,
                  'components/favourites.html',
                  {'new': new})


@login_required
def favourite_add(request, id):
    post = get_object_or_404(Blog, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



def delete_comment(request, pk, id):
    blog = get_object_or_404(Blog, id=pk)
    if pk:
        comment = Comment.objects.get(id=id)
        comment.delete()

        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'blog_detail.html')

