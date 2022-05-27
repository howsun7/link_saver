from django.test import TestCase
from links.forms import LinkForm
from links.models import Category, Link

class LinkFormTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='testcat')
		
		cls.categories = Category.objects.all()
		cls.good_form_data = {
			'url': 'http://example.com',
			'categories': cls.categories
		}

	def test_form_submission_without_categories_raises_error(self):
		data = {
			'url': 'http://example.com'
		}
		form = LinkForm(data=data)
		self.assertTrue(form.errors['categories'])

