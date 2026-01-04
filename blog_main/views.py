from django.shortcuts import render, get_object_or_404, redirect
from blogs import models
from about.models import About, Follow
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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

def register(request):
    if request.method>='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method >= 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')