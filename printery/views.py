import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django import forms

from printery.models import *
from printery.forms import *

# Create your views here.

def index(request):
    return render(request, "printery/index.html", {
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "printery/login.html", {
                "message": "Invalid username and/or password.", "form": UserForm()
            })
    else:
        return render(request, "printery/login.html", {
        "form": UserForm()
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "printery/register.html", {
                "message": user_form.errors, 'form': user_form
            })
    else:
        return render(request, "printery/register.html", {
        "form": UserForm()
        })
