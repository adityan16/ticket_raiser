from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, TicketForm
from .models import Ticket


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
    

@login_required
def dashboard(request):
    return render(request, 'tickets/dashboard.html')


@login_required
def create_ticket(request):
    error = ""
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_list')
        else:
            ticket = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user = request.user).order_by('-created_at')
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})