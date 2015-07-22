from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from blog.models import Post, Page
from taggit.models import Tag


def home(request):
    return page(request, 'home')


def page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
        return render(request, 'page.html', {'page': page})
    except:
        return not_found(request)


def not_found(request):
    page = Page.objects.get(slug='404')
    return render(request, 'page.html', {'page': page})


def blog(request):
    posts = Post.objects.all().order_by('-created')
    return paginate_posts(posts, request)


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__slug__in=[tag]).order_by('-created')
    return paginate_posts(posts, request)


def paginate_posts(posts, request):
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'posts': posts,
                  'tags': all_tags(), 'recent': recent()})


def blog_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', {'post': post,
                  'tags': all_tags(), 'recent': recent()})


def all_tags():
    tags = Tag.objects.all()
    tags = ['<a href="/blog/tag/{0}">{1}</a>'.format(t.slug, t) for t in tags]
    return ', '.join(tags)


def recent():
    return Post.objects.all().order_by('-created')[:5]
