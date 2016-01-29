from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post


def blog(request):
    posts = Post.objects.all().order_by('-created')
    return paginate_posts(posts, request)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = category.get_children()
    posts = Post.objects.filter(category__in=categories).order_by('-created')
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
    return render_with_sidebar(request, 'blog.html', {'posts': posts})


def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_with_sidebar(request, 'post.html', {'post': post})


def render_with_sidebar(request, template, content):
    categories = Category.objects.all()
    recent = Post.objects.order_by('-created')[:5]
    content['categories'] = categories
    content['recent'] = recent
    return render(request, template, content)
