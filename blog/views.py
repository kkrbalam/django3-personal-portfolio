from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    """
    Displays all blog posts
    """
    blogs = Blog.objects.order_by("-publish_date")
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {"details": details})
