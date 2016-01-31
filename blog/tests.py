from django.test import TestCase
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from blog.models import Category, Post


class BlogTestCase(TestCase):

    def setUp(self):
        programming = Category.objects.create(title='Programming')
        python = Category.objects.create(title='Python', parent=programming)
        django = Category.objects.create(title='Django', parent=python)

    def test_category_save_slugify(self):
        name = 'Programming'
        programming = Category.objects.get(title=name)
        self.assertEqual(programming.slug, slugify(name))

    def test_category_children(self):
        programming = Category.objects.get(title='Programming')
        self.assertEqual(len(programming.get_children()), 3)
