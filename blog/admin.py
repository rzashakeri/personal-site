from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
    list_filter = ["created_at"]
    ordering = ["created_at"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
