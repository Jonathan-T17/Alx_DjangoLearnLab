from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.other = User.objects.create_user(username='o', password='p')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_create_requires_login(self):
        url = reverse('blog:post_create')
        resp = self.client.get(url)
        self.assertNotEqual(resp.status_code, 200)  # should redirect to login

    def test_author_can_edit_delete(self):
        self.client.login(username='u', password='p')
        url_edit = reverse('blog:post_update', args=[self.post.pk])
        resp = self.client.get(url_edit)
        self.assertEqual(resp.status_code, 200)
        url_delete = reverse('blog:post_delete', args=[self.post.pk])
        resp = self.client.get(url_delete)
        self.assertEqual(resp.status_code, 200)

    def test_other_cannot_edit_delete(self):
        self.client.login(username='o', password='p')
        url_edit = reverse('blog:post_update', args=[self.post.pk])
        self.assertEqual(self.client.get(url_edit).status_code, 403)





class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.other = User.objects.create_user(username='o', password='p')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_post_comment_requires_login(self):
        url = reverse('blog:comment-create', args=[self.post.pk])
        resp = self.client.post(url, {'content': 'Nice post!'})
        # should redirect to login
        self.assertNotEqual(resp.status_code, 200)

    def test_create_comment(self):
        self.client.login(username='u', password='p')
        url = reverse('blog:comment-create', args=[self.post.pk])
        resp = self.client.post(url, {'content': 'Nice post!'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(self.post.comments.exists())
        self.assertEqual(self.post.comments.first().content, 'Nice post!')
