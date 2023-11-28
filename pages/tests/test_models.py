from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.text import slugify
from datetime import datetime, timedelta
from pages.models import SiteSettings, Page, About, ContactUs, SkillCategory, Skill, Project, SocialMedia, Education


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


class SkillCategoryTest(TestCase):
    def test_skill_category_str(self):
        skill_category = SkillCategory.objects.create(name='Programming', description='Programming skills')
        self.assertEqual(str(skill_category), 'Programming')


class SkillModelTest(TestCase):
    def test_skill_str(self):
        skill_category = SkillCategory.objects.create(name='Programming', description='Programming skills')
        skill = Skill.objects.create(category=skill_category, name='Python')
        self.assertEqual(str(skill), 'Python (Programming)')


class ProjectModelTest(TestCase):
    def test_project_str(self):
        page = Page.objects.create(title='Test Page', icon=SimpleUploadedFile("icon.png", b"file_content"))
        project = Project.objects.create(
            page=page,
            name='My Project',
            slug=slugify('My Project'),
            star_count=100,
            fork_count=50,
            short_description='A short description',
            description='A long description about the project.'
        )
        self.assertEqual(str(project), 'My Project')


class SocialMediaModelTest(TestCase):
    def test_social_media_str(self):
        social_media = SocialMedia.objects.create(
            name='Twitter',
            link='https://twitter.com/example',
            icon=SimpleUploadedFile("twitter.png", b"file_content")
        )
        self.assertEqual(str(social_media), 'Twitter')


class EducationModelTest(TestCase):

    def test_education_str(self):
        education = Education.objects.create(
            Degree='Bachelor of Science',
            School='University of Example',
            country='USA',
            city='Example City',
            start_date=datetime(2018, 9, 1),
            end_date=datetime(2022, 5, 30),
            present=False,
            description='Studied Computer Science.'
        )
        self.assertEqual(str(education), 'Bachelor of Science | University of Example')
