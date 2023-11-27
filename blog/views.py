from django.shortcuts import render, get_list_or_404
from django.views import View
from .models import Post


class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {"page": post}
        return render(request, "blog/post.html", context=context)


class TagView(View):
    def get(self, request, name):
        posts = get_list_or_404(Post, tags__name=name)
        context = {"posts": posts}
        return render(request, "blog/tag.html", context=context)
