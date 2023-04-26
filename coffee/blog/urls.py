from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('sign-up/', views.registerPage, name='sign_up'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update-user/<str:pk>/', views.updateUser, name="user_profile"),
    path('account/<str:pk>/', views.account, name='account'),
    path('account/delete-blog/<str:pk>/<str:id>', views.delete_blog, name='delete_blog'),
    path('blog/<str:pk>/', views.blog_detail, name='blog_detail'),
    path('delete-commnet/<str:pk>/<str:id>/', views.delete_comment, name='delete_comment'),
]
