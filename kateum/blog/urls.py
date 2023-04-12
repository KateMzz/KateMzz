from django.contrib import admin
from django.urls import path, include
from .views import PostListView, about, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    UserPostListView, Search, get_category
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('about/', about, name="about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user_posts"),
    path('search/', Search.as_view(), name="post_search"),
    path('category/<int:category_id>/', get_category, name='category'),
    path('like/', views.likes, name='likes')
    # path('like/<int:pk>', LikeView, name='like_post'),

]

