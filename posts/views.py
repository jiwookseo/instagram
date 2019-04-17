from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q


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


@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        return redirect('posts:index')
    post.delete()
    return redirect('posts:index')


def index(request):
    my_filter = Q(user=request.user)
    for user in request.user.followers.all():
        my_filter = my_filter | Q(user=user)
    posts = Post.objects.filter(my_filter).order_by('-id')
    form = CommentForm()
    return render(request, 'posts/index.html', {'posts':posts, 'form':form})


@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:index')


@login_required
@require_POST
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:index')


@login_required
@require_POST
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:index')
