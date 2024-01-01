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

    @property
    def visit_count(self):
        return Visit.objects.filter(post=self).count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Visit(models.Model):
    """
    View model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.ip_address}"

    class Meta:
        ordering = ['-created_at']
