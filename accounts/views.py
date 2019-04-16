from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
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
    return render(request, 'accounts/form.html', {'form':form})
    
    
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
    return render(request, 'accounts/form.html', {'form':form})
    

def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people':people})
    

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/form.html', {'form':form})
    

def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/form.html', {'form':form})
