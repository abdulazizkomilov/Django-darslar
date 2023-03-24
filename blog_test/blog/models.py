from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self) -> str:
        return self.title



