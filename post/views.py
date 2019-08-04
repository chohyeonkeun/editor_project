from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic.edit import CreateView

class PostCreate(CreateView):
    model = Post
    fields = ['title','text']
    template_name = 'post/create.html'