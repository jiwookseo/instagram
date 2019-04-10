from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:create')
        return
    else:
        form = PostForm()
        return render(request, 'posts/create.html', {'form':form})

def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'posts/index.html', {'posts':posts})