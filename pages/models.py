import datetime

from ckeditor.fields import RichTextField
from django.core import validators
from django.db import models
from django.db.models import CASCADE


class SiteSettings(models.Model):
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.domain} | {self.name}"


class Page(models.Model):
    title = models.CharField(max_length=200)
    icon = models.FileField(upload_to="icons/")
    slug = models.SlugField(max_length=300, unique=True)
    parent = models.ForeignKey("Page", on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class About(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    heading = models.CharField(max_length=200)
    body = RichTextField()

    def __str__(self):
        return self.heading


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


class ContactUs(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validators.validate_email])
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.email} | Time: {self.created_on}"


class Project(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    star_count = models.IntegerField()
    fork_count = models.IntegerField()
    short_description = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=300)
    icon = models.FileField(upload_to='icons/')

    def __str__(self):
        return self.name


class Education(models.Model):
    Degree = models.CharField(max_length=300)
    School = models.CharField(max_length=300)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    present = models.BooleanField(default=False)
    description = RichTextField()

    def __str__(self):
        return f"{self.Degree} | {self.School}"
