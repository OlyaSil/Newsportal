from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostFilter
from .forms import *

class PostsList(ListView):
    model = Post
    ordering = '-timedate'
    template_name = 'flatpages/default.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class ArticleCreate(CreateView):
    model = Post
    form_class = ArticleForm
    template_name = 'article_edit.html'
    success_url = reverse_lazy('post-list')
    def form_valid(self, form):
        form.instance.type = 'AR'
        return super().form_valid(form)

class ArticleUpdate(UpdateView):
    model = Post
    form_class = ArticleForm
    template_name = 'article_edit.html'
    success_url = reverse_lazy('post-list')

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post-list')

class NewsCreate(CreateView):
    model = Post
    form_class = NewsForm
    template_name = 'news_edit.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.type = 'NE'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    model = Post
    form_class = NewsForm
    template_name = 'news_edit.html'
    success_url = reverse_lazy('post-list')

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post-list')