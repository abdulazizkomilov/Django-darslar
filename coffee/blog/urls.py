from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('account/<str:pk>/', views.account, name='account'),
    path('blog/<str:pk>/', views.blog_detail, name='blog_detail'),
    path('delete-commnet/<str:pk>/<str:id>/', views.delete_comment, name='delete_comment'),
]
