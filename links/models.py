from django.db import models
from django.db.utils import IntegrityError
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=120, verbose_name='Category name', unique=True)

    def __str__(self):
        return self.name

class Link(TimeStampedModel):
    # title
    # short_desc / note
    url = models.URLField(verbose_name= 'URL')
    times_saved = models.PositiveIntegerField(default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.url
