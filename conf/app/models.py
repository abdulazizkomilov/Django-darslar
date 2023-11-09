from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    long = models.SmallIntegerField(default=0)
    start = models.DateField()

    def __str__(self) -> str:
        return self.name
