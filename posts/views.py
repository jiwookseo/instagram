from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form':form})


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        return redirect('posts:index')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/create.html', {'form':form})


def delete(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.user:
            return redirect('posts:index')
        post.delete()
    return redirect('posts:index')


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'posts/index.html', {'posts':posts})

@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:index')
