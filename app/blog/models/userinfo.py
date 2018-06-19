from django.db import models

from blog.models import bloguser

__all__ = (
    'UserInfo',
)

class UserInfo(models.Model):
    bloguser = models.OneToOneField(
        bloguser,
        on_delete=models.CASCADE,
    )
    address = models.TextField(max_length=50)
    phone_number = models.CharField(max_length=20)

