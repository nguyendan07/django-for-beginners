from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="test@email.com",
            password="secret"
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            auth=self.user,
        )
    
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.auth}", "testuser")
        self.assertEqual(f"{self.post.body}", "Nice body content")
    
    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Nice body content")
        self.assertTemplateUsed(resp, 'home.html')
    
    def test_post_detail_view(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/1000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, "A good title")
        self.assertTemplateUsed(resp, "post_detail.html")
