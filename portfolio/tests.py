from django.test import TestCase
from .models import Post


class ModelTesting(TestCase):

    def setUp(self):
        self.post = Post(title='My first post',
                         content='This is my first post',
                         image=None)

    def test_post_content(self):
        p = self.post
        self.assertTrue(isinstance(p, Post))
        self.assertEqual(str(p), 'My first post')
