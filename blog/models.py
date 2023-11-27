from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons/')
    slug = models.SlugField()
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']