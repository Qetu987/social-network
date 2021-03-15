from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class SimpleUser(AbstractUser):
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    date = models.DateTimeField(
        format("%Y-%m-%d"),
        auto_now_add=True,
    )


class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="dislikes")
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    date = models.DateTimeField(format("%Y-%m-%d"), auto_now_add=True)
