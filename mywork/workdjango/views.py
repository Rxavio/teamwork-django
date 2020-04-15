from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView   
)
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'workdjango/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Post
    # success_url = '/'
    success_message = "Article successfully added"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class PostDetailView(DetailView):
    model = Post     

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin, UpdateView):
    model = Post
    success_message = "Article successfully Updated"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
       
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False     

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

class UserPostListView(ListView):
    model = Post
    template_name = 'workdjango/user_posts.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')              