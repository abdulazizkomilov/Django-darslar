from django.db import models
from uuid import uuid4


class Person(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.full_name
