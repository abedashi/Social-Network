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

def profile(request):
    contact_list = Posts.objects.filter(user=request.user).annotate(
        is_liked=Exists(
            Likes.objects.filter(user=request.user, post=OuterRef('pk'))
        )).select_related('user').order_by("datetime")[::-1]

    followers = Follows.objects.filter(
        following_id=request.user,
    ).count()
    following = Follows.objects.filter(
        follower_id=request.user
    ).count()
        
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/profile.html", {
        "profile": User.objects.get(pk=request.user.id),
        "page_obj": page_obj,
        "followers": followers,
        "following": following
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
    ).select_related('user')

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

def post_view(request, post_id):
    # if(request.method == 'POST'):
    #     comment = request.POST["comment"]
    #     Comments.objects.create(
    #         entity = Entity.objects.create(
    #             user = request.user,
    #             text = comment
    #         ),
    #         post = Post.objects.get(entity_id=entity_id)
    #     )
    #     return redirect('post', entity_id)

    post = Posts.objects.get(post=post_id)
    comments = Comments.objects.filter(post=post)
    
    context = {}
    if request.user.is_authenticated:
        try:
            is_liked = Exists(Likes.objects.get(post=post_id, user=request.user))
        except:
            is_liked = False

        context["is_liked"] = is_liked

        comments = comments.annotate(
            is_liked = Exists(
                    Likes.objects.filter(user=request.user)
                )
        )
    context.update({
            "post": post
            # "comments": comments
        })
        
    return render(request, "network/post.html", context)

def profile_view(request, user_id):
    if request.user.is_authenticated:
        posts = Posts.objects.filter(user=user_id).annotate(
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

        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/profile.html", {
            "profile" : User.objects.get(pk=user_id),
            "page_obj": page_obj,
            "is_followed": is_followed,
            "followers" : followers,
            "following" : following
        })
    return HttpResponseRedirect(reverse("login"))

def follow(request, user_id):
    Follows.objects.create(follower=request.user, following_id=user_id)
    return HttpResponseRedirect(reverse("profileView"), kwargs={'user_id':user_id})

def unfollow(request, user_id):
    Follows.objects.get(follower=request.user, following_id=user_id).delete()
    return HttpResponseRedirect(reverse("profileView"), kwargs={'user_id':user_id})

def deletePost(request, post_id):
    try:
        Posts.objects.get(pk=post_id).delete()
    except:
        return HttpResponse(status=502)
    return HttpResponse(status=200)