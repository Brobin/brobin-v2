from django import template
from blog.models import Post, Category


register = template.Library()


@register.inclusion_tag('tags/_recent_posts.html')
def recent_posts():
    return {'recent': Post.objects.order_by('-created')[:5]}


@register.inclusion_tag('tags/_blog_categories.html')
def blog_categories():
    return {'categories': Category.objects.all()}
