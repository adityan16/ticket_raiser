from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm

# Create your views here.
def home(request):
    return render(request, 'tickets/home.html')


def login_view(request):
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error = "INVALID EMAIL OR PASSWORD"
        else:
            form = LoginForm()
        return render(request, 'tickets/login.html', {'form': form, 'error': error})
    
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'tickets/dashboard.html')
