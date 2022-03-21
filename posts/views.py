from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, CreateView, ListView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.


class Home(ListView):
    model= Post
    template_name = 'index.html'

class Post_detail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class Update_post(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields= ['title', 'body']

class Delete_post(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class Create_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'