from turtle import pos, title, update
from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model=Post
    template_name='home.html'

# Create your views here.

class BlogDetialView(DetailView):
    model= Post
    template_name='post_details.html'

class BlogCreateView(CreateView):
    model= Post
    template_name='post-new.html'
    fields='__all__'
class BlogUpdateView(UpdateView):
    model=Post
    template_name= 'post_edit.html'
    fields= ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name= 'post_delete.html'
    fields='__all__'
    success_url=reverse_lazy('home')