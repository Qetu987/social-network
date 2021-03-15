from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


"""
    Model of users from django db auth
"""
class SimpleUser(AbstractUser):
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


"""
    Model of posts with relations to users
"""
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


"""
    Model of like with relations to users and post
"""
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    date = models.DateTimeField(
        format("%Y-%m-%d"),
        auto_now_add=True,
    )


"""
    Model of dislike with relations to users and post
"""
class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="dislikes")
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    date = models.DateTimeField(format("%Y-%m-%d"), auto_now_add=True)
