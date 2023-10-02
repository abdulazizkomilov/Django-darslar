from django.urls import path
from . import views
from app.api.views import PersonAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('api/person/', PersonAPIView.as_view(), name='person'),
]
