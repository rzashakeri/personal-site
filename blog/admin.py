from django.contrib import admin

from blog.models import Post, Tag, Visit


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
    list_filter = ["created_at"]
    ordering = ["created_at"]
    search_fields = ["title"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["post", "ip_address", "created_at"]
    ordering = ["-created_at"]
