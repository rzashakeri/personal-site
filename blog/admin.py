from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "pub_date", "pub_date"]
    list_filter = ["pub_date"]
    ordering = ["pub_date"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
