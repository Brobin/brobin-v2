from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post


def blog(request):
    posts = Post.objects.all().order_by('-created')
    return paginate_posts(posts, request)


def archive(request, year):
    posts = Post.objects.filter(created__year=year)
    posts = posts.order_by('-created')
    return paginate_posts(posts, request)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = category.get_children()
    posts = Post.objects.filter(category__in=categories)
    posts = posts.order_by('-created')
    return paginate_posts(posts, request)


def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(content__icontains=query) | 
        Q(title__icontains=query)
    )
    posts = posts.order_by('-created')
    return paginate_posts(posts, request, query)


def paginate_posts(posts, request, search=None):
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    payload = {'posts': posts, 'search': search}
    return render(request, 'blog/blog.html', payload)


def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
