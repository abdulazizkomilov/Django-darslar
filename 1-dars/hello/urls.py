from django.urls import path
from .views import hello, sana_vaqt, Welcome

urlpatterns = [
    path('', hello, name='home'),
    path('time/', sana_vaqt, name='time'),
    path('class/', Welcome.as_view(), name='index')
]
