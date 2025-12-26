from django.shortcuts import render
from blogs import models

def home(request):
    categories = models.Category.objects.all()
    featured_posts = models.Blog.objects.filter(is_featured = True, status='Published').order_by('updated_at')
    recent_posts = models.Blog.objects.filter(is_featured = False, status='Published').order_by('updated_at')
    context = {
        'categories' : categories,
        'featured_posts' : featured_posts,
        'recent_posts' : recent_posts,
    }
    return render(request, 'home.html', context)

