from django.contrib import admin
from .models import Category, Blog, Comment

# to make the slug field automatic
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured', )

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin) # also register BlogAdmin here for the slug field to apply
admin.site.register(Comment)