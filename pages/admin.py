from django.contrib import admin

from portfolio.pages.models import Page, About, SkillCategory, Skill, ContactUs, Project, SiteSettings, SocialMedia, Education

admin.site.register(SiteSettings)

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "parent", "is_parent"]

admin.site.register(Page, PageAdmin)
admin.site.register(About)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(ContactUs)
admin.site.register(Project)
admin.site.register(SocialMedia)
admin.site.register(Education)
