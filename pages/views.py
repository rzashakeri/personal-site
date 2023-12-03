from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from blog.models import Post
from pages.forms import ContactUsModelForm
from pages.models import About
from pages.models import Page
from pages.models import Project
from pages.models import SiteSettings
from pages.models import SkillCategory
from pages.models import SocialMedia


class HomeView(View):
    """ """
    def get(self, request):
        """Handle GET requests for the view.

        Redirect to the "home" URL if the current path is "/home/".
        Retrieve the "home" page object and the site settings object.
        Render the index.html template with the context data.

        :param request:

        """

        # Redirect to the "home" URL if the current path is "/home/"
        if request.path == "/home/":
            return redirect(reverse("home"))

        # Retrieve the "home" page object
        home = get_object_or_404(Page, slug="home")

        # Retrieve the site settings object
        portfolio = SiteSettings.objects.first()

        # Create a context dictionary with the page and portfolio objects
        context = {"page": home, "portfolio": portfolio}

        # Render the index.html template with the context data
        return render(request, "pages/index.html", context=context)


class AboutView(View):
    """Retrieves the "about-us" page from the database along with the first About object."""

    def get(self, request):
        """

        :param request:

        """
        # Retrieve the "about-us" page from the database
        about_us = get_object_or_404(Page, slug="about-us")

        # Retrieve the first About object from the database
        about = About.objects.first()

        # Create a context dictionary with the retrieved objects
        context = {"page": about_us, "about": about}

        # Render the "about.html" template with the context dictionary and return the response
        return render(request, "pages/about.html", context=context)


class ContactUsView(View):
    """This view handles the contact us page.

    It renders the contact.html template with the following context:

    - contact_us_form: An instance of the ContactUsModelForm
    - page: The Page object with slug "contact-us"


    """

    def get(self, request):
        """

        :param request:

        """
        # Create an instance of the ContactUsModelForm
        contact_us_form = ContactUsModelForm()

        # Retrieve the Page object with slug "contact-us"
        contact_us = get_object_or_404(Page, slug="contact-us")

        # Create a dictionary with the ContactUsModelForm and the Page object
        context = {"contact_us_form": contact_us_form, "page": contact_us}

        # Render the "contact.html" template with the context dictionary
        return render(request, "pages/contact.html", context=context)

    def post(self, request):
        """

        :param request:

        """
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
            return redirect(reverse("home"))

        # If the form data is not valid, render the contact.html template with the context
        return render(request, "pages/contact.html", context=context)


class ProjectsView(View):
    """ """
    def get(self, request):
        """

        :param request:

        """
        page = Page.objects.get(slug="projects")
        projects = Project.objects.all().order_by("-star_count")
        context = {"page": page, "projects": projects}
        return render(request, "pages/projects.html", context=context)


class ProjectView(View):
    """ """
    def get(self, request, slug):
        """

        :param request:
        :param slug:

        """
        try:
            project = Project.objects.get(slug=slug)
            page = project.page
            context = {"page": page, "project": project}
            return render(request, "pages/project.html", context=context)
        except ObjectDoesNotExist:
            return render(request, "404.html")


class SkillsView(View):
    """ """
    def get(self, request):
        """

        :param request:

        """
        page = Page.objects.get(slug="skills")
        skill_category = SkillCategory.objects.all().order_by("name")
        context = {"page": page, "skill_category": skill_category}
        return render(request, "pages/skills.html", context=context)


class SideBarView(TemplateView):
    """ """
    template_name = "shared/sidebar.html"
    ordering = ["is_parent"]

    def get_context_data(self, **kwargs):
        """

        :param **kwargs:

        """
        pages = Page.objects.all().order_by("-is_parent", "title")
        posts = Post.objects.all()
        kwargs["pages"] = pages
        kwargs["posts"] = posts
        return super(SideBarView, self).get_context_data(**kwargs)


def render_navbar_title(request):
    """

    :param request:

    """
    portfolio = SiteSettings.objects.first()
    context = {"portfolio": portfolio}
    return render(request, "shared/partials/navbar_title.html", context=context)


def breadcrumb_title(request):
    """

    :param request:

    """
    portfolio = SiteSettings.objects.first()
    context = {"portfolio": portfolio}
    return render(request, "shared/partials/breadcrumb_title.html", context=context)


def render_social_media(request):
    """

    :param request:

    """
    social_medias = SocialMedia.objects.all()
    context = {"social_medias": social_medias}
    return render(request, "shared/social_media.html", context=context)


def render_footer(request):
    """

    :param request:

    """
    site = SiteSettings.objects.first()
    context = {"site": site}
    return render(request, "shared/footer.html", context=context)
