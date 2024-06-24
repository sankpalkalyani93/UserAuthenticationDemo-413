from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authenticationapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authenticationapp/login.html', {'form': form})
    else: 
        form = AuthenticationForm()
        return render(request, 'authenticationapp/login.html', {'form':form})


def home_view(request):
    return render(request, 'authenticationapp/home.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'authenticationapp/password_change.html', {'form': form})