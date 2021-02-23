from django.shortcuts import render
from django.views.generic import ListView , CreateView
from .models import Blog_post

class BlogTestView(ListView):
    model = Blog_post
    template_name = 'blog_app/blog_test.html'

class BlogCreateView(CreateView):
    model = Blog_post
    template_name = 'blog_app/create_test.html'
    fields = ['title', 'text', 'author']