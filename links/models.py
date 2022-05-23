from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Link(TimeStampedModel):
    url = models.URLField()
    times_saved = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)


