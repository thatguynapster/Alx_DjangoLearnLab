from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm


def home(request):
    return render(request, "blog/base.html")


# Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


# Login View (Django’s built-in)
class CustomLoginView(LoginView):
    template_name = "blog/login.html"


# Logout View (Django’s built-in)
class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"


# Profile View
@login_required
def profile(request):
    return render(request, "blog/profile.html")
