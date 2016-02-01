from django import template
from blog.models import Post, Category


register = template.Library()


@register.inclusion_tag('blog/tags/_blog_recent.html')
def blog_recent():
    return {'recent': Post.objects.order_by('-created')[:5]}


@register.inclusion_tag('blog/tags/_blog_categories.html')
def blog_categories():
    return {'categories': Category.objects.all()}


@register.inclusion_tag('blog/tags/_blog_archive.html')
def blog_archive():
    years = [p.created.year for p in Post.objects.all()]
    years = set(years)
    return {'years': years}
