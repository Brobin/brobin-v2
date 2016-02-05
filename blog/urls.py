from django.conf.urls import url
from blog.feeds import BlogPostRssFeed, BlogPostAtomFeed
from blog import views


urlpatterns = [
    url(r'^$', views.blog, name='blog_index'),
    url(r'^feed/rss/$', BlogPostRssFeed()),
    url(r'^feed/atom/$', BlogPostAtomFeed()),
    url(r'^search/$', views.search, name='blog_search'),
    url(r'^([a-zA-Z\-]*)/$', views.category, name='blog_category'),
    url(r'^archive/([0-9]{4})/$', views.archive, name='blog_archive'),
    url(r'^[0-9]{4}/[0-9]{2}/(?P<slug>.*)/$', views.blog_post, name='blog_post'),
]
