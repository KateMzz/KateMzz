import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST

from .models import Post, Category
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


@login_required
def likes(request):
    if request.method == "POST":
        result = ''
        id = request.POST.get('postid')
        post = get_object_or_404(Post, id=id)
        if post.post_likes.filter(id=request.user.id).exists():
            post.post_likes.remove(request.user)
            post.post_likes_count -= 1
            result = post.post_likes_count
            post.save()
        else:
            post.post_likes.add(request.user)
            post.post_likes_count += 1
            result = post.post_likes_count
            post.save()
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': "the request is not supported"})


def index(request):
    posts = Post.objects.order_by('-date_posted')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, "blog/index.html", context)



def about(request):
    return render(request, 'blog/about.html', {"about": "about page"})


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class Search(ListView):
    # model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(title__iregex=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def get_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'category': category
    }

    return render(request, 'blog/category_posts.html', context)