from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .models import User, Follows, Posts, Comments, Likes

def index(request):
    if request.method == "POST":
        # Attempt to add post
        post = request.POST["addPost"]

        # If form is empty
        if not post:
            messages.warning(request, "Please fill out the field!")
            return HttpResponseRedirect(reverse("index"))
        
        # Insert new post to Posts
        addPost = Posts.objects.create(
            userID = request.user,
            post = post
        )
        addPost.save()
        messages.success(request, "Post Added Successfully")
        return HttpResponseRedirect(reverse("index"))
    return render(request, "network/index.html", {
            "posts": Posts.objects.all().order_by("datetime")[::-1]
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request):
    return render(request, "network/profile.html", {
        "myPost": Posts.objects.filter(userID=request.user).order_by("datetime")[::-1]
    })

def following(request):
    # posts = Posts.objects.filter(
    #     posts__user__follower__in = Follows.objects.filter(follower=request.user)
    # ).select_related('posts')
    return render(request, "network/following.html", {
        # "myFollowers": "posts"
        # "myFollowers": Posts.objects.filter(followID=Follows.objects.filter(follower=request.user)).select_related('followID')
    })