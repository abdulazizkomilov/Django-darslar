from django.contrib import admin
from .models import *

# class CommentInLine(admin.StackedInline):
#     model = Comment
#     extra = 0

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

admin.site.register(Music)
admin.site.register(Video)