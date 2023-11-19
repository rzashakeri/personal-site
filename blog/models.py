from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=100)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']