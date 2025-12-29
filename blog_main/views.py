from django.shortcuts import render, get_object_or_404
from blogs import models
from about.models import About, Follow
def home(request):
    categories = models.Category.objects.all()
    featured_posts = models.Blog.objects.filter(is_featured = True, status='Published').order_by('updated_at')
    recent_posts = models.Blog.objects.filter(is_featured = False, status='Published').order_by('updated_at')
    about = About.objects.get()
    follow = Follow.objects.all()
    context = {
        'categories' : categories,
        'featured_posts' : featured_posts,
        'recent_posts' : recent_posts,
        'about' : about,
        'follow' : follow
    }
    return render(request, 'home.html', context)


