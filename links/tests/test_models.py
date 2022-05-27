from django.db.utils import IntegrityError
from django.test import TestCase

from links.models import Link, Category


class CategoryModelTest(TestCase):
    def test_cannot_create_category_with_the_same_name(self):
        category_name = 'testing'
        Category.objects.create(name=category_name)
        with self.assertRaises(IntegrityError):
            Category.objects.create(name=category_name)


class LinkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = 'https://example.com'

    def test_the_first_time_saving_link_saves_link_with_time_saved_of_1(self):
        link = Link.objects.create(url=self.url)
        self.assertEqual(link.times_saved, 1)
