
from django.contrib import admin
from django.urls import path, include

from app.api.views import CourseViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'courses', CourseViewset)
# router.register(r'students', StudentViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
