from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user, name='user'),
    path('add/', views.AddView.as_view(), name='add'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]
