from django.urls import path
from api.api import views

urlpatterns = [
    path('', views.employee_list, name='employee'),
    path('employee/<uuid:pk>/', views.employee_detail, name='detail'),
]
