from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count, Q
from . import models
from about.models import About, Follow

# Create your views here.
def posts_by_category(request, category_id):
    try:
        category = get_object_or_404(models.Category, id=category_id)
    except:
        return redirect('home')
    posts = models.Blog.objects.filter(category=category, status='Published')
    categories = models.Category.objects.all()
    context={
        'posts': posts,
        'category': category,
        'categories':categories
    }
    return render(request, 'post_by_category.html', context)

def blog(request, slug):
    blog = get_object_or_404(models.Blog, slug=slug)
    context = {
        'blog' : blog,
    }
    return render(request, 'blog.html', context)

def search(request):
    about = About.objects.get()
    follow = Follow.objects.all()
    query = request.GET.get('keyword')
    if query:
        posts = models.Blog.objects.filter(
            Q(title__icontains=query) | 
            Q(short_description__icontains=query) | 
            Q(blog_body__icontains=query),
            status='Published'
        )
    else:
        posts = models.Blog.objects.none()
    categories = models.Category.objects.all()
    context = {
        'posts': posts,
        'query': query,
        'categories': categories,
        'about' : about,
        'follow' : follow
    }
    return render(request, 'search.html', context)