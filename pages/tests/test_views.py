from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.core.mail import outbox
from django.contrib.messages import get_messages
from django.conf import settings
from captcha.conf import settings as captcha_settings

from pages.forms import ContactUsModelForm
from pages.models import Page, SiteSettings, About, ContactUs
from pages.views import ContactUsView


class HomeViewTest(TestCase):
    def setUp(self):
        # Create a test page and site settings
        self.page = Page.objects.create(
            slug="home",
            title="test",
            icon=SimpleUploadedFile("icon.png", b"file_content"),
        )
        self.site_settings = SiteSettings.objects.create()

    def test_redirect_if_path_is_home(self):
        # Issue a GET request to the view with path "/home/"
        response = self.client.get("/home/", follow=True)

        # Check that the response is a redirect to the "home" URL
        self.assertRedirects(response, reverse("index"))

    def test_get_view_with_valid_path(self):
        # Issue a GET request to the view with a valid path
        response = self.client.get("/", follow=True)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, "pages/index.html")

        # Check that the context contains the expected page and portfolio objects
        self.assertEqual(response.context["page"], self.page)
        self.assertEqual(response.context["portfolio"], self.site_settings)


class AboutViewTest(TestCase):
    def test_get_about_page(self):
        # Create a test "about-us" page in the database
        about_us = Page.objects.create(
            title="About Us",
            slug="about-us",
            icon=SimpleUploadedFile("icon.png", b"file_content"),
        )
        # Create a test About object in the database
        about = About.objects.create(
            page=about_us, heading="About", body="This is the about page."
        )

        # Get the about page
        response = self.client.get(reverse("about"), follow=True)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, "pages/about.html")

        # Check that the correct context is used
        self.assertEqual(response.context["page"], about_us)
        self.assertEqual(response.context["about"], about)

    def test_get_about_page_with_no_about_object(self):
        # Delete the about object from the database
        About.objects.all().delete()

        # Get the about page
        response = self.client.get(reverse("about"), follow=True)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 404)

        # Check that the about object is not in the context
        self.assertNotIn("about", response.context)


class ContactUsViewTest(TestCase):
    def setUp(self):
        self.home_page = Page.objects.create(
            slug="home",
            title="test",
            icon=SimpleUploadedFile("icon.png", b"file_content"),
        )
        self.page = Page.objects.create(
            title="Contact Us",
            slug="contact-us",
            icon=SimpleUploadedFile("icon.png", b"file_content"),
        )
        captcha_settings.CAPTCHA_TEST_MODE = True
        self.url = reverse("contact_us")

    def test_get_contact_us_page(self):
        # Test that the contact us page is rendered correctly
        response = self.client.get(reverse("contact_us"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")
        self.assertIn("contact_us_form", response.context)
        self.assertIn("page", response.context)

    def test_post_valid_contact_form(self):
        # Test that a valid contact form submission redirects to the home page and sends an email
        data = {
            "first_name": "Test User first name",
            "last_name": "Test User last name",
            "email": "testuser@example.com",
            "message": "Test message",
            "captcha_0": "8e10ebf60c5f23fd6e6a9959853730cd69062a15",
            "captcha_1": "PASSED",
        }
        response = self.client.post(reverse("contact_us"), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Message sent successfully")
        self.assertIn("page", response.context)

    def test_post_invalid_contact_form(self):
        # Test that an invalid contact form submission does not redirect to the home page and does not send an email
        data = {
            "name": "",
            "email": "invalidemail",
            "message": "",
        }
        response = self.client.post(reverse("contact_us"), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")
        self.assertEqual(len(outbox), 0)

    def test_contact_us_form_instance(self):
        # Test that the contact us form instance is created correctly
        form = ContactUsModelForm()
        self.assertIsInstance(form, ContactUsModelForm)

    def test_contact_us_view_instance(self):
        # Test that the contact us view instance is created correctly
        view = ContactUsView()
        self.assertIsInstance(view, ContactUsView)
