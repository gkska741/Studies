from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Article(models.Model):
    title = CharField(max_length=100)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    image = models.ImageField(upload_to = 'origins/', blank = True)
    image_thumbnail = ImageSpecField(
        format = 'JPEG',
        processors = [ResizeToFill(100, 50)],
        source='image',
        options={'quality': 90}
    )

    def __str__(self):
        return self.title