from django.test import TestCase
from navigation.models import MenuItem, SubMenuItem


class NavigationTestCase(TestCase):

    def setUp(self):
        MenuItem.objects.create(
            title='Projects', link='/projects', order=2
        )
        MenuItem.objects.create(
            title='Admin', link='/admin', order=3
        )
        
        self.blog_menu = MenuItem.objects.create(
            title='Blog', link='/', order=1
        )
        self.example_menu = MenuItem.objects.create(
            title='Example', link='/', base_url='//example.com', order=1
        )

        SubMenuItem.objects.create(
            title='Something1',
            link='/blog/something1',
            order=1,
            menu=self.blog_menu
        )
        SubMenuItem.objects.create(
            title='Something2',
            link='/blog/something2',
            order=2,
            menu=self.blog_menu
        )
        SubMenuItem.objects.create(
            title='Something3',
            link='/blog/something3',
            order=3,
            menu=self.blog_menu
        )

    def test_sub_menu_items(self):
        self.assertTrue(self.blog_menu.has_sub_items)

    def test_correct_ordering(self):
        order = -1
        for item in self.blog_menu.sub_menu_items:
            self.assertTrue(item.order > order)
            order = item.order

    def test_menu_sub_items(self):
        self.assertEqual(self.blog_menu.num_sub_menu_items, 3)

    def test_menu_item_name(self):
        self.assertEqual(str(self.blog_menu), 'Blog')
        item = SubMenuItem.objects.get(title='Something1')
        self.assertEqual(str(item), 'Blog Something1')

    def test_base_url(self):
        self.assertEqual(self.example_menu.url, '//example.com/')

    def test_url(self):
        self.assertEqual(self.blog_menu.url, '/')
