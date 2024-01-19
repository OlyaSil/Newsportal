from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class PostsList(ListView):
    model = Post
    ordering = '-timedate'
    template_name = 'flatpages/default.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
