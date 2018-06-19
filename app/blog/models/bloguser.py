from django.db import models

__all__ = (
    'Bloguser',
)

class Bloguser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        related_name='my_friends',
        symmetrical=False,
        blank=True,
    )
    CHOICES_RELATION_TYPE = (
        ('B', 'Block'),
    )

    def __str__(self):
        return self.name

