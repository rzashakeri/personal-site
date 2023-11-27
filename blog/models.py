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
    tag = models.ManyToManyField("Tag", related_name="posts")

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


class Comment(models.Model):
    """
    Comment model
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
