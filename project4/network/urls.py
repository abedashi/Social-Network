
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("profile/<int:user_id>", views.profile_view, name="profileView"),
    path("following", views.following, name="following"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>", views.unfollow, name="unfollow"),
    path("post/like/<int:post_id>", views.like, name="like"),
    path("post/unlike/<int:post_id>", views.unlike, name="unlike"),
    path("delete/<int:post_id>", views.deletePost, name="delete")
]
