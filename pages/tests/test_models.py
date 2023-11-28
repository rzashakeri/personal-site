from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from pages.models import SiteSettings, Page, About, ContactUs


class SiteSettingsModelTest(TestCase):
    def test_site_settings_str(self):
        site_settings = SiteSettings.objects.create(
            domain='example.com',
            name='My Site',
            job_title='Software Developer',
            footer_text='Copyright © 2023 My Site',
            footer_link='https://example.com/contact/'
        )
        self.assertEqual(str(site_settings), 'example.com | My Site')


class PageModelTest(TestCase):
    def test_page_str(self):
        page = Page.objects.create(title='Test Page', icon=SimpleUploadedFile("icon.png", b"file_content"))
        self.assertEqual(str(page), 'Test Page')


class AboutModelTest(TestCase):
    def test_about_str(self):
        page = Page.objects.create(title='Test Page', icon=SimpleUploadedFile("icon.png", b"file_content"))
        about = About.objects.create(page=page, heading='About Me', body='Some details about me.')
        self.assertEqual(str(about), 'About Me')



class ContactUsModelTest(TestCase):
    def test_contact_us_str(self):
        page = Page.objects.create(title='Test Page', icon=SimpleUploadedFile("icon.png", b"file_content"))
        contact_us = ContactUs.objects.create(
            page=page,
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            message='Hello, this is a test message.'
        )
        expected_str = f"From: {contact_us.email} | Time: {contact_us.created_on}"
        self.assertEqual(str(contact_us), expected_str)


