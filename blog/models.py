from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons/')
    slug = AutoSlugField(populate_from='title')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
