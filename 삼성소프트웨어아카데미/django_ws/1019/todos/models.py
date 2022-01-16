from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)