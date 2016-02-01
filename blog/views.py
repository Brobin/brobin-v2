from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
from blog.managers import PostManager


def blog(request):
    posts = Post.visible_posts.all()
    return paginate_posts(posts, request)


def archive(request, year):
    posts = Post.visible_posts.filter(created__year=year)
    return paginate_posts(posts, request)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = category.get_children()
    posts = Post.visible_posts.filter(category__in=categories)
    return paginate_posts(posts, request)


def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.visible_posts.filter(
            Q(content__icontains=query) | 
            Q(title__icontains=query)
        )
    else:
        posts = Post.visible_posts.all()
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
