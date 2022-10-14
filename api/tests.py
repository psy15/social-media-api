from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            user=cls.user,
            title="A good title",
            description="Nice description",
            number_of_likes=0
        )

    def test_post_model(self):

        self.assertEqual(self.post.user.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.description, "Nice description")
        self.assertEqual(self.post.number_of_likes, 0)
        self.assertEqual(str(self.post), "A good title")
