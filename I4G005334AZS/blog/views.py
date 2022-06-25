from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    models = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


