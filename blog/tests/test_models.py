from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Post, Tag
class PostModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')
        self.post = Post.objects.create(
            title='Test Post',
            icon=SimpleUploadedFile('icon.png', b''),
            content='Test content'
        )
        self.post.tags.add(self.tag1, self.tag2)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_ordering(self):
        post1 = Post.objects.create(
            title='Post 1',
            icon=SimpleUploadedFile('icon_1.png', b''),
            content='Test content'
        )
        post2 = Post.objects.create(
            title='Post 2',
            icon=SimpleUploadedFile('icon_2.png', b''),
            content='Test content'
        )
        self.assertGreater(post2.created_at, post1.created_at)

    def test_post_tags(self):
        self.assertIn(self.tag1, self.post.tags.all())
        self.assertIn(self.tag2, self.post.tags.all())

    def test_post_slug(self):
        self.assertEqual(self.post.slug, 'test-post')

    def test_post_content(self):
        self.assertEqual(self.post.content, 'Test content')

    def test_post_created_at(self):
        self.assertIsNotNone(self.post.created_at)

    def test_post_updated_at(self):
        self.assertIsNotNone(self.post.updated_at)

    def test_post_tags_blank(self):
        post = Post.objects.create(
            title='Post without tags',
            icon=SimpleUploadedFile('icon.png', b''),
            content='Test content'
        )
        self.assertEqual(post.tags.count(), 0)



class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name='Test Tag')

    def test_str_representation(self):
        self.assertEqual(str(self.tag), 'Test Tag')

    def test_slug_is_populated_from_name(self):
        self.assertEqual(self.tag.slug, 'test-tag')

    def test_description_is_blank(self):
        self.assertEqual(self.tag.description, '')

    def test_created_at_is_auto_generated(self):
        self.assertIsNotNone(self.tag.created_at)

    def test_updated_at_is_auto_generated(self):
        self.assertIsNotNone(self.tag.updated_at)

    def test_ordering_by_name(self):
        tag1 = Tag.objects.create(name='Another Tag')
        tag2 = Tag.objects.create(name='Third Tag')
        tags = Tag.objects.all()
        self.assertEqual(tags[0], tag1)
        self.assertEqual(tags[1], self.tag)
        self.assertEqual(tags[2], tag2)