
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("following", views.following, name="following"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>", views.unfollow, name="unfollow"),
    path("post/like/<int:post_id>", views.like, name="like"),
    path("post/unlike/<int:post_id>", views.unlike, name="unlike"),
    path("delete/<int:post_id>", views.deletePost, name="delete"),
    path("post_view/<int:post_id>", views.post_view, name="postView"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit"),
    path("edit_profile/<int:user_id>", views.edit_profile, name="editProfile")
]
