# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect after register
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def home_view(request):
    return render(request, 'users/home.html')

def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

# Diet Page
@login_required
def diet_page(request):
    return render(request, 'users/diet.html')

# Run Tracking Page
@login_required
def run_tracking_page(request):
    return render(request, 'users/run_tracking.html')

# Social Connection Page
@login_required
def connect_page(request):
    return render(request, 'users/connect.html')