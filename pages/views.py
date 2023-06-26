from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from portfolio.pages.forms import ContactUsModelForm
from portfolio.pages.models import SiteSettings, Page, About, ContactUs, Project, SkillCategory, SocialMedia


class HomeView(View):
    def get(self, request):
        if request.path == "/home/":
            return redirect(reverse('home'))
        home = Page.objects.get(slug="home")
        portfolio = SiteSettings.objects.first()
        context = {
            "page": home,
            "portfolio": portfolio
        }
        return render(request, "pages/index.html", context=context)


class AboutView(View):
    def get(self, request):
        about_us = Page.objects.get(slug="about-us")
        about = About.objects.first()
        context = {
            "page": about_us,
            "about": about
        }
        return render(request, "pages/about.html", context=context)


class ContactUsView(View):
    def get(self, request):
        contact_us_form = ContactUsModelForm()
        contact_us = Page.objects.get(slug="contact-us")
        context = {
            "contact_us_form": contact_us_form,
            "page": contact_us
        }
        return render(request, "pages/contact.html", context=context)

    def post(self, request):
        contact_us_form = ContactUsModelForm(request.POST)
        contact_us = Page.objects.get(slug="contact-us")
        context = {
            "contact_us_form": contact_us_form,
            "page": contact_us
        }
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.success(request, 'Message sent successfully', extra_tags='fa-sharp fa-solid fa-square-check fa-xl')
            return render(request, "pages/contact.html", context=context)
        return render(request, "pages/contact.html", context=context)


class ProjectsView(View):
    def get(self, request):
        page = Page.objects.get(slug="projects")
        projects = Project.objects.all().order_by("-star_count")
        context = {
            "page": page,
            "projects": projects
        }
        return render(request, "pages/projects.html", context=context)


class ProjectView(View):
    def get(self, request, slug):
        try:
            project = Project.objects.get(slug=slug)
            page = project.page
            context = {
                "page": page,
                "project": project
            }
            return render(request, "pages/project.html", context=context)
        except ObjectDoesNotExist:
            return render(request, "404.html")


class SkillsView(View):
    def get(self, request):
        page = Page.objects.get(slug="skills")
        skill_category = SkillCategory.objects.all()
        context = {
            "page": page,
            "skill_category": skill_category
        }
        return render(request, "pages/skills.html", context=context)


class SideBarView(TemplateView):
    template_name = "shared/sidebar.html"
    ordering = ['is_parent']

    def get_context_data(self, **kwargs):
        pages = Page.objects.all().order_by("-is_parent", "title")
        kwargs['pages'] = pages
        return super(SideBarView, self).get_context_data(**kwargs)


def render_navbar_title(request):
    portfolio = SiteSettings.objects.first()
    context = {
        "portfolio": portfolio
    }
    return render(request, "shared/partials/navbar_title.html", context=context)


def breadcrumb_title(request):
    portfolio = SiteSettings.objects.first()
    context = {
        "portfolio": portfolio
    }
    return render(request, "shared/partials/breadcrumb_title.html", context=context)


def render_social_media(request):
    social_medias = SocialMedia.objects.all()
    context = {
        'social_medias': social_medias
    }
    return render(request, 'shared/social_media.html', context=context)
