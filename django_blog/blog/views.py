from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserUpdateForm


class UserLoginView(LoginView):
    template_name = "blog/login.html"


from django.contrib.auth.views import LogoutView

class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"
    next_page = "blog:login"
    http_method_names = ["get", "post", "head"]  # allow GET



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("blog:profile")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})

def home(request):
    return render(request, "blog/base.html")


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("blog:profile")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})
