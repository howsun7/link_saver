from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=120, verbose_name='Category name')

    def __str__(self):
        return self.name

class Link(TimeStampedModel):
    # short_desc
    url = models.URLField(verbose_name= 'URL')
    times_saved = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)


