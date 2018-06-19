from django.db import models

from blog.models.bloguser import Bloguser


class Post(models.Model):
     user = models.ForeignKey(
        Bloguser,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    content=models.TextField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class PostLIke(models.Model):
    user = models.ForeignKey(
        Bloguser,
        on_delete=models.CASCADE,
        related_name='post_likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(
        Bloguser,
        on_delete=models.CASCADE
    )