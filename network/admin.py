from django.contrib import admin
from .models import SimpleUser, Post, Like, Dislike


@admin.register(SimpleUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "last_login"]
    list_display_links = ["id", "username"]
    search_fields = ["id", "username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "desc", "user"]
    list_display_links = ["id", "title"]
    search_fields = ["id", "title"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "date"]
    list_display_links = ["id", "user"]
    search_fields = ["id", "user"]


@admin.register(Dislike)
class DisikeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "date"]
    list_display_links = ["id", "user"]
    search_fields = ["id", "user"]
