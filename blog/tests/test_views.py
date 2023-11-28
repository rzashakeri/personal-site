from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Tag

class PostViewTest(TestCase):
    def setUp(self):
        # Create a sample post for testing
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post content.",
            slug="test-post",
            icon=SimpleUploadedFile('icon.png', b''),
        )

    def test_post_view(self):
        # Get the URL for the PostView with the sample post's slug
        url = reverse('post', kwargs={'slug': self.post.slug})

        # Simulate a GET request to the PostView
        response = self.client.get(url,  follow=True)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the post object is present in the context
        self.assertIn('page', response.context)

        # Check if the rendered HTML contains the post title
        self.assertContains(response, self.post.title)

    def test_post_view_with_invalid_slug(self):
        # Get a URL with an invalid slug that does not exist in the database
        url = reverse('post', kwargs={'slug': 'non-existent-slug'})

        # Simulate a GET request to the PostView with an invalid slug
        response = self.client.get(url,  follow=True)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)


class TagViewTest(TestCase):
    def setUp(self):
        # Create a sample tag and posts for testing
        self.tag = Tag.objects.create(name="Test Tag")
        self.post1 = Post.objects.create(title="Post 1", content="This is post 1.", slug="post-1")
        self.post2 = Post.objects.create(title="Post 2", content="This is post 2.", slug="post-2")

        # Associate the posts with the sample tag
        self.post1.tags.add(self.tag)
        self.post2.tags.add(self.tag)

    def test_tag_view(self):
        # Get the URL for the TagView with the sample tag's name
        url = reverse('tag', kwargs={'name': self.tag.name})

        # Simulate a GET request to the TagView
        response = self.client.get(url, follow=True)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the tag name is present in the context
        self.assertIn('posts', response.context)

        # Check if the rendered HTML contains the post titles
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)

    def test_tag_view_with_invalid_name(self):
        # Get a URL with an invalid tag name that does not exist in the database
        url = reverse('tag', kwargs={'name': 'non-existent-tag'})

        # Simulate a GET request to the TagView with an invalid tag name
        response = self.client.get(url, follow=True)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)
