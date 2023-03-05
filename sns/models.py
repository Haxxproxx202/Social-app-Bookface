from django.db import models
from django.contrib.auth.models import User

REACTIONS = (
    (1, "love"),
    (2, "like"),
    (3, "surprised"),
    (4, "shocked"),
    (5, "sad"),
    (6, "angry")
)


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="uploaded/")
    likes = models.ManyToManyField(User, related_name="likes_post")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)


class Friend(models.Model):
    users = models.ManyToManyField(User)
    is_confirmed = models.BooleanField(default=False)


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    friends = models.ManyToManyField('self')








