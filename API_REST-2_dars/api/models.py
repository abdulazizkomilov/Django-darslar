from django.db import models
from uuid import uuid4


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self) -> str:
        return self.full_name
