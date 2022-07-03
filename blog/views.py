from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView


class ListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'allPosts'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'details.html'