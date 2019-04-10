from django.shortcuts import render, redirect
from .forms import PostForm


def create(request):
    if request.method == "POST":
        return
    else:
        form = PostForm()
        return render(request, 'posts/create.html', {'form':form})
