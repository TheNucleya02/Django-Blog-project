from django import forms
from blogs.models import Category, Blog

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class PostForms(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['slug', 'author']
        fields = "__all__"

