from django import template
from ..models import Post, Category


register = template.Library()


@register.inclusion_tag('blog/tags/_blog_recent.html')
def blog_recent():
    return {'recent': Post.visible_posts.order_by('-created')[:5]}


@register.inclusion_tag('blog/tags/_blog_categories.html')
def blog_categories():
    return {'categories': Category.objects.order_by('title')}


@register.inclusion_tag('blog/tags/_blog_archive.html')
def blog_archive():
    posts = Post.visible_posts.all()
    return {'posts': posts}
