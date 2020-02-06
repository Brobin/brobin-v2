from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Category, Post


def posts(request, filter_kwargs={}, search=None):
    objects = Post.objects.filter(**filter_kwargs)
    paginator = Paginator(objects, 10)
    try:
        objects = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    context = {'posts': objects, 'search': search}
    return render(request, 'blog/blog.html', context)


@cache_page(60 * 15)
def blog(request):
    return posts(request)


@cache_page(60 * 15)
def archive(request, year):
    return posts(request, {'created__year': year})


@cache_page(60 * 15)
def category(request, slug):
    categories = get_object_or_404(Category, slug=slug).get_children()
    return posts(request, {'category__in': categories})


def search(request):
    query = request.GET.get('q')
    if query:
        return posts(request, {'content__icontains': query}, search=query)
    return posts(request, search=query)


@cache_page(60 * 60)
def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
