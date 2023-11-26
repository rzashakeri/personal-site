from django.shortcuts import render
from django.views import View
from .models import Post


class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {"page": post}
        return render(request, "blog/post.html", context=context)
