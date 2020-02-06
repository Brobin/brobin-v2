from django.conf.urls import url
from .feeds import BlogPostRssFeed, BlogPostAtomFeed
from .views import(
    blog,
    search,
    category,
    archive,
    blog_post
)


urlpatterns = [
    url(r'^$', blog, name='blog_index'),
    url(r'^feed/rss/$', BlogPostRssFeed()),
    url(r'^feed/atom/$', BlogPostAtomFeed()),
    url(r'^search/$', search, name='blog_search'),
    url(r'^([a-zA-Z\-]*)/$', category, name='blog_category'),
    url(r'^archive/([0-9]{4})/$', archive, name='blog_archive'),
    url(r'^[0-9]{4}/[0-9]{2}/(?P<slug>.*)/$', blog_post, name='blog_post'),
]
