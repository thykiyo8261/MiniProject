from django.contrib import messages
from django.shortcuts import render, redirect

from Accounts.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):
    user = RegisterForm(request.POST or None)
    if user.is_valid():
        print(user.cleaned_data)
        user.save()
        user = RegisterForm()

    context = {'obj':user}
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect username or password')
    context = {}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def redirect_to_home(request):
    return redirect('login')
        