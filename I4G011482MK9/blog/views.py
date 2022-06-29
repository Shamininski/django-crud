from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from msilib.schema import ListView
from django.shortcuts import render
from .models import Post, blog

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

