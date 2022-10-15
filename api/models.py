from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    followers = models.IntegerField(default=0)
    followings = models.IntegerField(default=0)

    def __str__(self):
        return self.email


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class LikePost(models.Model):
    post_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class FollowUser(models.Model):
    follower = models.IntegerField()
    user = models.IntegerField()

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey("Post",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
