from django.test import TestCase
from links.models import Link, Category

class CategoryTestCase(TestCase):
    def test_cannot_create_category_with_the_same_name(self):
        category_name = 'testing'
        Category.objects.create(name=category_name)
        with self.assertRaises(Exception):
            Category.objects.create(name=category_name)
