from django.urls import path
from .views import front_page, single, search

app_name = 'blog'

urlpatterns = [
    path('', front_page, name='home'),
    path('search/', search, name='search'),
    path('post-detail/<slug:slug>/', single, name='single')
]
