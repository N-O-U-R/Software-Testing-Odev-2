from django.urls import path
from .views import blog_list, blog_detail, add_post

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('add/', add_post, name='add_post'),
    path('<int:post_id>/', blog_detail, name='blog_detail'),
]
