from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Major, Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


def index(request):
    majors = Major.objects.prefetch_related("profiles").all().order_by("name")
    return render(request, "core/index.html", {"majors": majors})


def profile_detail(request, pk):
    profile = get_object_or_404(
        Profile.objects.select_related("major")
        .prefetch_related("documents", "passports", "modules"),
        pk=pk
    )

    context = {
        "profile": profile,
        "documents": profile.documents.all(),
        "passports": profile.passports.all(),
        "modules": profile.modules.all(),
    }
    return render(request, "core/profile_detail.html", context)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("core:index")
    else:
        form = RegisterForm()
    return render(request, "core/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("core:index")
    else:
        form = LoginForm()
    return render(request, "core/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("core:login")


@login_required
def user_profile_view(request):
    return render(request, "core/user_profile.html", {"user": request.user})
