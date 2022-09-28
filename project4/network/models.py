from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    backgroundColor = models.TextField(default="rgb(203, 68, 74)")
    image = models.ImageField(null=True, default="profile.png", upload_to="images")

class Follows(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="followers")

    def __str__(self):
        return f"{self.follower}, {self.following}"

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=datetime.now())
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.user}, {self.text}, {self.datetime})"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"({self.user}, {self.post}, {self.comment})"

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="liker")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name="postLiked")

    def __str__(self):
        return f"({self.user}, {self.post}"