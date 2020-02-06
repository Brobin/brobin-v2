from django.urls import path
from .feeds import BlogPostRssFeed, BlogPostAtomFeed
from .views import(
    blog,
    search,
    category,
    archive,
    blog_post
)


urlpatterns = [
    path('feed/rss/', BlogPostRssFeed()),
    path('feed/atom/', BlogPostAtomFeed()),
    path('search/', search, name='blog_search'),
    path('<slug>/', category, name='blog_category'),
    path('archive/<year>/', archive, name='blog_archive'),
    path('<int:year>/<int:month>/<slug>/', blog_post, name='blog_post'),
    path('', blog, name='blog_index'),
]
