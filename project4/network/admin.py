from django.contrib import admin
from .models import User, Follows, Posts, Likes, Comments

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "image")

class FollowsAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "following")

class PostsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "text", "datetime")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "comment")

class LikesAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Follows, FollowsAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Likes, LikesAdmin)
