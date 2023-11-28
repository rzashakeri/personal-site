from django.test import TestCase
from pages.models import SiteSettings



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
