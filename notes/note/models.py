from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ('title',)