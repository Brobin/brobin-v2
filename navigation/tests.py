from django.test import TestCase
from navigation.models import MenuItem, SubMenuItem


class NavigationTestCase(TestCase):

    def setUp(self):
        MenuItem.objects.create(title='Projects', link='/projects', order=2)
        MenuItem.objects.create(title='Admin', link='/admin', order=3)
        blog_menu = MenuItem.objects.create(title='Blog', link='/', order=1)

        SubMenuItem.objects.create(
            title='Something1',
            link='/blog/something1',
            order=1,
            menu=blog_menu
        )
        SubMenuItem.objects.create(
            title='Something2',
            link='/blog/something2',
            order=2,
            menu=blog_menu
        )
        SubMenuItem.objects.create(
            title='Something3',
            link='/blog/something3',
            order=3,
            menu=blog_menu
        )

    def test_sub_menu_items(self):
        blog = MenuItem.objects.get(title='Blog')
        self.assertTrue(blog.has_sub_items)

    def test_correct_ordering(self):
        blog = MenuItem.objects.get(title='Blog')
        order = -1
        for item in blog.sub_menu_items:
            self.assertTrue(item.order > order)
            order = item.order

    def test_menu_sub_items(self):
        blog = MenuItem.objects.get(title='Blog')
        self.assertEqual(len(blog.sub_menu_items), 3)
