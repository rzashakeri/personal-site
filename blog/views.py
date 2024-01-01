from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View

from utils import get_client_ip
from .models import Post, Visit


class PostView(View):
    """
    Post View
    """
    def get(self, request, slug):
        # Retrieve the post object with the given slug from the database
        post = get_object_or_404(Post, slug=slug)

        # create visit object
        Visit.objects.get_or_create(post=post, ip_address=get_client_ip(request))

        # Create a context dictionary with the post object
        context = {"page": post}

        # Render the blog/post.html template with the context data
        return render(request, "blog/post.html", context=context)


class TagView(View):
    """
    Tag View
    """
    def get(self, request, name):
        # Retrieve posts with the specified tag name
        posts = get_list_or_404(Post, tags__name=name)

        # Create a context dictionary with the retrieved posts
        context = {"posts": posts}

        # Render the tag.html template with the context data
        return render(request, "blog/tag.html", context=context)