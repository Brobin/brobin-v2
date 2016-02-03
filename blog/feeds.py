from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from blog.models import Post


class BlogPostRssFeed(Feed):
    title = "Brobin's Blog"
    link = "/blog"
    description = "Techonology, Programming, and more"

    def items(self):
        return Post.visible_posts.all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.preview().replace('\r\n',' ')


class BlogPostAtomFeed(BlogPostRssFeed):
    feed_type = Atom1Feed
    subtitle = BlogPostRssFeed.description
