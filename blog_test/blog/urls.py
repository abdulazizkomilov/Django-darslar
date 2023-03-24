from django.urls import path
from .views import front_page, single

app_name = 'blog'

urlpatterns = [
    path('', front_page, name='home'),
    path('post-detail/<slug:slug>/', single, name='single')
]