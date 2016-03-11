from django.test import TestCase, Client
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date, datetime
from blog.feeds import BlogPostRssFeed
from blog.models import Category, Post


class BlogTestCase(TestCase):

    def setUp(self):
        programming = Category.objects.create(title='Programming')
        python = Category.objects.create(title='Python', parent=programming)
        django = Category.objects.create(title='Django', parent=python)
        user = User.objects.create(username='tobin')
        Post.objects.create(title='test', content='', visible=False,
                            author=user, category=programming)

    def test_category_save_slugify(self):
        name = 'Programming'
        programming = Category.objects.get(title=name)
        self.assertEqual(programming.slug, slugify(name))

    def test_category_children(self):
        programming = Category.objects.get(title='Programming')
        self.assertEqual(len(programming.get_children()), 3)

    def test_visible_post_manager(self):
        post = Post.objects.get(title='test')
        queryset = Post.visible_posts.all()
        self.assertTrue(post not in queryset)

    def test_blog_feed(self):
        feed = BlogPostRssFeed()
        items = feed.items()
        self.assertTrue( len(items) <= 20)


class BlogRequestTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        programming = Category.objects.create(title='Programming')
        user = User.objects.create(username='tobin')
        Post.objects.create(title='test', content='', visible=True,
                            author=user, category=programming,
                            created=datetime.now())

    def test_blog_index(self):
        response = self.client.get(reverse('blog_index'))
        self.assertEqual(response.status_code, 200)

    def test_blog_category(self):
        url = reverse('blog_category', args=['programming'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_archive(self):
        year = date.today().year
        url = reverse('blog_archive', args=[year])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post(self):
        url = reverse('blog_post', kwargs={'slug': 'test'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_search(self):
        url = reverse('blog_search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_search_query(self):
        url = reverse('blog_search') + '?q=test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_invalid_page(self):
        url = reverse('blog_index') + '?page=69'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
