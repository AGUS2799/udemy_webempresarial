from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/blog.html", context)

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, "blog/category.html", context)