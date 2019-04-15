from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Login success, welcome {}'.format(user.username))
            return redirect(request.GET.get('next') or 'posts:index')
        else:
            messages.success(request, 'Login fail, check your username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
    
    
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout success')
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Register Success, welcome {}'.format(user.username))
            return redirect('posts:index')
        else:
            messages.success(request, 'Login fail, check your username or password')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/login.html', {'form':form})