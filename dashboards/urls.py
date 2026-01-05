from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('my_posts/', views.my_posts, name='my_posts'),
    path('my_posts/create_post', views.createPost, name='create_post'),
    path('my_posts/edit/<int:pk>', views.editPost, name='edit_post'),
    path('my_posts/delete/<int:pk>', views.deletePost, name='delete_post'),

    path('categories/', views.categories, name='categories'),
    path('categories/add', views.categoriesAdd, name='categories_add'),
    path('categories/edit/<int:pk>', views.categoriesEdit, name='categories_edit'),
    path('categories/delete/<int:pk>', views.categoriesDelete, name='categories_delete')

]