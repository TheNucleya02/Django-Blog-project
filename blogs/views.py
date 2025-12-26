from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count, Q
from . import models

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