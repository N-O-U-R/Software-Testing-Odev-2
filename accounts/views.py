from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page.
        else:
            return render(request, 'index.html', {'login_error': 'Invalid login credentials'})
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not fname or not email or not password:
            return render(request, 'index.html', {'register_error': 'Email and password must be set.'})
        username = email  # Using email as username
        try:
            user = User.objects.create_user( first_name = fname ,username=username, email=email, password=password)
            login(request, user)
            return redirect('home')  # Redirect after registration
        except Exception as e:
            return render(request, 'index.html', {'register_error': 'Email already exists'})
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')