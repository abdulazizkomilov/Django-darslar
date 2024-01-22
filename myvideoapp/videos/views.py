from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoStreamingView(APIView):
    def get(self, request, *args, **kwargs):
        video_id = kwargs.get('pk')
        video = Video.objects.get(pk=video_id)
        video_path = video.video_file.path
        wrapper = FileWrapper(open(video_path, 'rb'))
        response = StreamingHttpResponse(wrapper, content_type='video/mp4')
        response['Content-Disposition'] = f'inline; filename="{video.title}.mp4"'
        return response
