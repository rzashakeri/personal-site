from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

from pages.models import Page, SiteSettings  # Replace 'yourapp' with the actual name of your app

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
