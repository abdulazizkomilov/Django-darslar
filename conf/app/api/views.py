from app.models import Course
from app.api.serializers import CourseSerializer
from rest_framework import viewsets


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
