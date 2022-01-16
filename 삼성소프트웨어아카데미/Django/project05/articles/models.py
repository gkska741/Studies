from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

# Create your models here.
def articles_image_path(instance, filename):
    return f'user_{instance.pk}/{filename}'

    
class Article(models.Model):

    title = CharField(max_length=100)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    image = models.ImageField(upload_to = 'origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors = [ResizeToFill(100, 50)],
        format = 'JPEG',
        options = {'quality': 90}

    )
    def __str__(self):
        return self.title