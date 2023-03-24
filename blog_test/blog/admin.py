from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'id',]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Articles, ArticlesAdmin)


