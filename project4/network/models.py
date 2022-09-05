from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    number_of_post = models.IntegerField(default=0)
    number_of_followers = models.IntegerField(default=0)
    number_of_following = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

class Follows(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="following")

    def __str__(self):
        return f"{self.follower}, {self.following}"

class Posts(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.userID}, {self.post}, {self.datetime})"

class Comments(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postID = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"({self.userID}, {self.postID}, {self.comment})"

class Likes(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="liker")
    postID = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name="postLiked")
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.userID}, {self.postID}, {self.is_liked})"