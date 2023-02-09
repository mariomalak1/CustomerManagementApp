from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from accounts.decorators import is_not_authenticated
from django.contrib.auth.models import Group
from django.contrib.auth.views import login_required
# Create your views here.

@is_not_authenticated
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_ = form.cleaned_data.get("username")

            # add the user to customers group
            customers_group = Group.objects.get(name='customers')
            customers_group.user_set.add(user_)

            messages.add_message(request, messages.SUCCESS, f"{user_} you are registered Successfully")
            return redirect("login")
    else:
        form = CreateUserForm()
    context = {"form":form}
    return render(request, "users/register.html", context)

@is_not_authenticated
def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user_ = User.objects.filter(username = username).first()
            if user_ is not None:
                login(request, user_)
                messages.add_message(request, messages.SUCCESS, "Login Done Successfully")
                return redirect("dashboard")
            else:
                messages.add_message(request, messages.WARNING, "Login failed!")
    else:
        form = LoginForm()
    context = {'form':form}

    return render(request, "users/login_page.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required

def accountUser(request):
    return render(request, "users/account.html")