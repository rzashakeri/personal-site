from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from blog.models import Post
from pages.forms import ContactUsModelForm
from pages.models import (
    SiteSettings,
    Page,
    About,
    Project,
    SkillCategory,
    SocialMedia,
)


class HomeView(View):
    def get(self, request):
        """
        Handle GET requests for the view.
        Redirect to the "home" URL if the current path is "/home/".
        Retrieve the "home" page object and the site settings object.
        Render the index.html template with the context data.
        """
        # Redirect to the "home" URL if the current path is "/home/"
        if request.path == "/home/":
            return redirect("index")

        # Retrieve the "home" page object from cache or database
        home = cache.get("home")
        if not home:
            home = get_object_or_404(Page, slug="home")
            cache.set("home", home)

        # Retrieve the site settings object from cache or database
        portfolio = cache.get("site_settings")
        if not portfolio:
            portfolio = SiteSettings.objects.first()
            cache.set("site_settings", portfolio)

        # Create a context dictionary with the page and portfolio objects
        context = {"page": home, "portfolio": portfolio}
        # Render the index.html template with the context data
        return render(request, "pages/index.html", context=context)


class AboutView(View):
    """
    Retrieves the "about-us" page from the database along with the first About object.
    """

    def get(self, request):
        # Retrieve the "about-us" page from the database
        about_us = get_object_or_404(Page, slug="about-us")

        # Retrieve the first About object from the database
        about = About.objects.first()

        # Create a context dictionary with the retrieved objects
        context = {"page": about_us, "about": about}

        # Render the "about.html" template with the context dictionary and return the response
        return render(request, "pages/about.html", context=context)


class ContactUsView(View):
    """
    This view handles the contact us page.

    It renders the contact.html template with the following context:

    - contact_us_form: An instance of the ContactUsModelForm
    - page: The Page object with slug "contact-us"
    """

    def get(self, request):
        # Create an instance of the ContactUsModelForm
        contact_us_form = ContactUsModelForm()

        # Retrieve the Page object with slug "contact-us"
        contact_us = get_object_or_404(Page, slug="contact-us")

        # Create a dictionary with the ContactUsModelForm and the Page object
        context = {"contact_us_form": contact_us_form, "page": contact_us}

        # Render the "contact.html" template with the context dictionary
        return render(request, "pages/contact.html", context=context)

    def post(self, request):
        # Create an instance of the ContactUsModelForm with the POST data
        contact_us_form = ContactUsModelForm(request.POST)

        # Get the Page object with the slug "contact-us"
        contact_us = get_object_or_404(Page, slug="contact-us")

        # Create a dictionary with the form and page objects as context
        context = {"contact_us_form": contact_us_form, "page": contact_us}

        # Check if the form data is valid
        if contact_us_form.is_valid():
            # Save the form data
            contact_us_form.save()

            # Display a success message to the user
            messages.success(
                request,
                "Message sent successfully",
                extra_tags="fa-sharp fa-solid fa-square-check fa-xl",
            )

            # Redirect the user to the home page
            return redirect(reverse("index"))

        # If the form data is not valid, render the contact.html template with the context
        return render(request, "pages/contact.html", context=context)


class ProjectsView(View):
    """
    A class-based view for handling the GET request to display projects.

    Attributes:
        None

    Methods:
        get: Retrieves the page and projects, creates a context dictionary, and renders the projects.html template.

    """

    def get(self, request):
        # Get the page with slug "projects"
        page = get_object_or_404(Page, slug="projects")

        # Get all projects and order them by star count in descending order
        projects = Project.objects.all().order_by("-star_count")

        # Create a context dictionary with the page and projects
        context = {"page": page, "projects": projects}

        # Render the projects.html template with the context
        return render(request, "pages/projects.html", context=context)


class ProjectView(View):
    """
    A class-based view that displays a project page.

    Attributes:
        None

    Methods:
        get: Retrieves the project object based on the slug provided, retrieves the page associated with the project, prepares the context data to be passed to the template, and renders the project.html template with the provided context.

    """

    def get(self, request, slug):
        # Retrieve the project object based on the slug provided
        project = get_object_or_404(Project, slug=slug)

        # Retrieve the page associated with the project
        page = project.page

        # Prepare the context data to be passed to the template
        context = {"page": page, "project": project}

        # Render the project.html template with the provided context
        return render(request, "pages/project.html", context=context)


class SkillsView(View):
    """
    Retrieves the page object with the slug "skills" and the skill categories ordered by name.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "skills.html" template with the page and skill category objects in the context.
    """

    def get(self, request):
        # Retrieve the page object with the slug "skills"
        page = get_object_or_404(Page, slug="skills")

        # Retrieve all skill categories and order them by name
        skill_category = SkillCategory.objects.all().order_by("name")

        # Create a context dictionary with the page and skill category objects
        context = {"page": page, "skill_category": skill_category}

        # Render the "skills.html" template with the context
        return render(request, "pages/skills.html", context=context)


class SideBarView(TemplateView):
    template_name = "shared/sidebar.html"
    ordering = ["is_parent"]

    def get_context_data(self, **kwargs):
        pages = Page.objects.all().order_by("-is_parent", "title")
        posts = Post.objects.all()
        kwargs["pages"] = pages
        kwargs["posts"] = posts
        return super(SideBarView, self).get_context_data(**kwargs)


def render_navbar_title(request):
    portfolio = SiteSettings.objects.first()
    context = {"portfolio": portfolio}
    return render(request, "shared/partials/navbar_title.html", context=context)


def breadcrumb_title(request):
    portfolio = SiteSettings.objects.first()
    context = {"portfolio": portfolio}
    return render(request, "shared/partials/breadcrumb_title.html", context=context)


def render_social_media(request):
    social_medias = SocialMedia.objects.all()
    context = {"social_medias": social_medias}
    return render(request, "shared/social_media.html", context=context)


def render_footer(request):
    site = SiteSettings.objects.first()
    context = {"site": site}
    return render(request, "shared/footer.html", context=context)
