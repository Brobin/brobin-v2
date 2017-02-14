from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from blog.decorators import paginate_posts
from blog.models import Category, Post


@paginate_posts
def blog(request):
    return Post.visible_posts.all()


@paginate_posts
def archive(request, year):
    return Post.visible_posts.filter(created__year=year)


@paginate_posts
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = category.get_children()
    return Post.visible_posts.filter(category__in=categories)


@paginate_posts
def search(request):
    query = request.GET.get('q')
    if query:
        return Post.visible_posts.filter(
            Q(content__icontains=query) |
            Q(title__icontains=query)
        )
    return Post.visible_posts.all()


def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
