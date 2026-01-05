from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dashboards.forms import CategoryForms, PostForms
from django.utils.text import slugify

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.count()
    total_post = Blog.objects.count()
    context = {
        'category_count' : category_count,
        'total_posts' : total_post,
        
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def my_posts(request):
    my_posts = Blog.objects.filter(author=request.user).order_by('updated_at')

    context = {
    'my_posts' : my_posts
    }
    return render(request, 'dashboard/my_posts.html', context)

@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login')
def categoriesAdd(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForms()
    context = {
        'form' : form
    }
    return render(request, 'dashboard/category_add.html', context)

@login_required(login_url='login')
def createPost(request):
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   # 👈 automatically set
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('my_posts')
    else:
        form = PostForms()
    context = {
        'form' : form
    }
    return render(request, 'dashboard/create_post.html', context)

@login_required(login_url='login')
def categoriesEdit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForms(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForms(instance=category)
    context = {
        'form' : form,
        'category' : category
    }
    return render(request, 'dashboard/edit_category.html', context)

@login_required(login_url='login')
def categoriesDelete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

@login_required(login_url='login')
def editPost(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method=="POST":
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_posts')
    else:
        form=PostForms(instance=post)
    context = {
        'form' : form
    }
    return render(request, 'dashboard/edit_posts.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('my_posts')