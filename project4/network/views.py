from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Exists, OuterRef, F,  Count
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *

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
            user = request.user,
            text = post
        )
        addPost.save()
        messages.success(request, "Post Added Successfully")
        return HttpResponseRedirect(reverse("index"))

    if request.user.is_authenticated:
        posts = Posts.objects.annotate(
            is_liked=Exists(
                Likes.objects.filter(user=request.user, post=OuterRef('id'))
            )
        ).select_related('user').order_by("datetime")[::-1]

        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, "network/index.html", {
            'page_obj': page_obj
        })

    posts = Posts.objects.all().order_by("datetime")[::-1]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {'page_obj': page_obj})


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

def profile(request, user_id):
    contact_list = Posts.objects.filter(user=user_id).annotate(
        is_liked=Exists(
            Likes.objects.filter(user=user_id, post=OuterRef('pk'))
        )).select_related('user').order_by("datetime")[::-1]

    is_followed = Follows.objects.filter(
        follower=request.user,
        following=user_id
    ).exists()

    followers = Follows.objects.filter(
        following_id=user_id,
    ).count()
    following = Follows.objects.filter(
        follower_id=user_id
    ).count()
    user = User.objects.get(pk=user_id)
    cover = "style=background-color:{}".format(user.backgroundColor)

    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/profile.html", {
        "profile": user,
        "page_obj": page_obj,
        "is_followed": is_followed,
        "followers": followers,
        "following": following,
        "cover": cover
    })

def following(request):
    posts = Posts.objects.filter(
        user__followers__in = Follows.objects.filter(follower = request.user)
    ).annotate(
        is_liked=Exists(
            Likes.objects.filter(
                user=request.user, post=OuterRef('pk')
            )
        )
    ).select_related('user').order_by("datetime")[::-1]

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/following.html", {'page_obj': page_obj})

def like(request, post_id):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    Likes.objects.create(
        post = Posts.objects.get(id=post_id),
        user = request.user
    )
    return HttpResponse(status=204)

def unlike(request, post_id):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    Likes.objects.get(
        post = Posts.objects.get(id=post_id),
        user = request.user
    ).delete()
    return HttpResponse(status=204)

def follow(request, user_id):
    Follows.objects.create(follower=request.user, following_id=user_id)
    return HttpResponseRedirect(reverse("profile", kwargs={'user_id':user_id}))

def unfollow(request, user_id):
    Follows.objects.get(follower=request.user, following_id=user_id).delete()
    return HttpResponseRedirect(reverse("profile", kwargs={'user_id':user_id}))

def deletePost(request, post_id):
    try:
        Posts.objects.get(pk=post_id).delete()
    except:
        return HttpResponse(status=502)
    return HttpResponse(status=200)

def post_view(request, post_id):
    if request.method == "POST":
        comment = request.POST["comment"]
        Comments.objects.create(
            user=request.user,
            post=Posts.objects.get(pk=post_id),
            comment=comment
        )
        return HttpResponseRedirect(reverse("postView", kwargs={'post_id': post_id}))

    post = Posts.objects.get(pk=post_id)
    try:
        is_liked = Exists(Likes.objects.get(post=post_id, user=request.user))
    except:
        is_liked = False
    
    comments = Comments.objects.filter(post=post_id).order_by("datetime")[::-1]
    return render(request, "network/post.html", {
        "post": post,
        "is_liked": is_liked,
        "comments": comments
    })

@csrf_exempt
def edit(request, post_id):
    post = Posts.objects.get(pk=post_id);
    data = json.loads(request.body)
    if data.get("new_post") is not None:
        post.text = data["new_post"]
    post.save()
    return HttpResponse(status=204)

def edit_profile(request, user_id):
    if request.method == "POST":
        email = request.POST["mail"]
        bio = request.POST["bio"]
        color = request.POST["color"]
        file = request.POST["file"]

        user = User.objects.get(pk=user_id)
        user.backgroundColor = color
        if not email and not bio and not file:
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
        if not email and not bio:
            user.image = file
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
        if not bio and file:
            user.email = email
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
        if not email and not file:
            user.bio = bio
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
        if not email:
            user.bio = bio
            user.image = file
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
        if not bio:
            user.email = email
            user.image = file
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
        if not file:
            user.email = email
            user.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))

        user.email = email
        user.bio = bio
        user.image = file
        user.save()
        return HttpResponseRedirect(reverse("profile", kwargs={"user_id": user_id}))
