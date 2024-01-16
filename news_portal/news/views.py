from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class PostsList(ListView):
    model = Post
    ordering = '-timedate'
    template_name = 'flatpages/default.html'
    context_object_name = 'posts'



# Create your views here.
