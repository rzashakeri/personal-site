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

