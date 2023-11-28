from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from pages.models import SiteSettings, Page


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

