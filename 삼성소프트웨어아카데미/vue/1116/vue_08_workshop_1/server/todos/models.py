from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)