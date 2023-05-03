from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.home, name='home'),
    path('add-post', views.createPost, name='createPost'), 
    path('blog/', views.blog, name='blog'),
    path('user-profile/<str:pk>/', views.users, name='user'),
    path('sign-up/', views.registerPage, name='sign_up'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update-user/<str:pk>/', views.updateUser, name="user_profile"),
    path('account/<str:pk>/', views.account, name='account'),
    path('account/delete-blog/<str:pk>/<str:id>', views.delete_blog, name='delete_blog'),
    path('blog/<str:pk>/', views.blog_detail, name='blog_detail'),
    path('update-blog/<str:pk>/', views.blogUpdate, name='update_blog'),
    path('like-blog/<str:pk>/', views.like_blog, name='like_blog'),
    path('deslike-blog/<str:pk>/', views.deslike_blog, name='deslike_blog'),
    path('follow-blog/<str:pk>/', views.follow_blog, name='follow_blog'),
    path('unfollow-blog/<str:pk>/', views.unfollow_blog, name='unfollow_blog'),
    path('delete-commnet/<str:pk>/<str:id>/', views.delete_comment, name='delete_comment'),
]
