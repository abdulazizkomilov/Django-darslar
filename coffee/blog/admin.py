from django.contrib import admin
from .models import Blog, Comment, Userprofile


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Userprofile)
