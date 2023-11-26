from django.contrib import admin

from pages.models import Page, About, SkillCategory, Skill, ContactUs, Project, SiteSettings, SocialMedia, Education

admin.site.register(SiteSettings)

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "parent", "is_parent"]
    list_filter = ["is_parent"]
    ordering = ["is_parent"]
    search_fields = ["title"]

admin.site.register(Page, PageAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ["page", "heading"]
    search_fields = ["title"]

admin.site.register(About, AboutAdmin)


admin.site.register(Skill)
admin.site.register(ContactUs)
admin.site.register(Project)
admin.site.register(SocialMedia)
admin.site.register(Education)
