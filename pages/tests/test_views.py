from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core.mail import outbox
from django.utils.html import strip_tags
from captcha.conf import settings as captcha_settings

from pages.forms import ContactUsModelForm
from pages.models import Page, SiteSettings, About
from pages.views import ContactUsView


class HomeViewTest(TestCase):
    def setUp(self):
        # Create a test page and site settings
        self.page = Page.objects.create(slug='home', title="test", icon=SimpleUploadedFile("icon.png", b"file_content"))
        self.site_settings = SiteSettings.objects.create()

    def test_redirect_if_path_is_home(self):
        # Issue a GET request to the view with path "/home/"
        response = self.client.get('/home/', follow=True)

        # Check that the response is a redirect to the "home" URL
        self.assertRedirects(response, reverse('home'), status_code=301)

    def test_get_view_with_valid_path(self):
        # Issue a GET request to the view with a valid path
        response = self.client.get('/', follow=True)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'pages/index.html')

        # Check that the context contains the expected page and portfolio objects
        self.assertEqual(response.context['page'], self.page)
        self.assertEqual(response.context['portfolio'], self.site_settings)


class AboutViewTest(TestCase):
    def test_get_about_page(self):
        # Create a test "about-us" page in the database
        about_us = Page.objects.create(title="About Us", slug="about-us",
                                       icon=SimpleUploadedFile("icon.png", b"file_content"))
        # Create a test About object in the database
        about = About.objects.create(page=about_us, heading="About", body="This is the about page.")

        # Get the about page
        response = self.client.get(reverse('about'), follow=True)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'pages/about.html')

        # Check that the correct context is used
        self.assertEqual(response.context['page'], about_us)
        self.assertEqual(response.context['about'], about)

    def test_get_about_page_with_no_about_object(self):
        # Delete the about object from the database
        About.objects.all().delete()

        # Get the about page
        response = self.client.get(reverse('about'), follow=True)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 404)

        # Check that the about object is not in the context
        self.assertNotIn('about', response.context)


class ContactUsViewTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Contact Us", slug='contact-us',
                                        icon=SimpleUploadedFile("icon.png", b"file_content"))
        captcha_settings.CAPTCHA_TEST_MODE = True
        self.url = reverse('contact_us')

    def test_get_method(self):
        response = self.client.get(self.url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')
        self.assertIsInstance(response.context['contact_us_form'], ContactUsModelForm)
        self.assertEqual(response.context['page'], self.page)
    def test_get_contact_us_page(self):
        # Test that the contact us page is rendered correctly
        response = self.client.get(reverse("contact_us"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")
        self.assertIn("contact_us_form", response.context)
        self.assertIn("page", response.context)
