from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField

# Create your models here.
class Article(models.Model):
    title = CharField(max_length=100)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

