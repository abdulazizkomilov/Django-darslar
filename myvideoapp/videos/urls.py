from django.urls import path
from .views import VideoList, VideoDetail, VideoStreamingView

urlpatterns = [
    path('videos/', VideoList.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('videos/<int:pk>/stream/',
         VideoStreamingView.as_view(), name='video-stream'),
]
