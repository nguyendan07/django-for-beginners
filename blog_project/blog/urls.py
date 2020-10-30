from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('posts/', BlogListView.as_view(), name='post_list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new')
]
