from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def paginate_posts(view):
    def wrapper(request, *args, **kwargs):
        objects = view(request, *args, **kwargs)
        paginator = Paginator(objects, 10)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        search = request.GET.get('q') or None
        payload = {'posts': objects, 'search': search}
        return render(request, 'blog/blog.html', payload)
    return wrapper
