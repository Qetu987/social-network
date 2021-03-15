from rest_framework import serializers
from .models import Dislike, Post, Like, SimpleUser


"""
    Serializer for get query like
"""
class LikeSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Like
        fields = ("user", "date")


"""
    Serializer for create like
"""
class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


"""
    Serializer for get query dislike
"""
class DislikeSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Dislike
        fields = ("user", "date")


"""
    Serializer for create dislike
"""
class DislikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"


"""
    Serializer for get query to post
"""
class PostSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True, read_only=True)
    dislikes = DislikeSerializer(many=True, read_only=True)

    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


"""
    Serializer for post query to post
"""
class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


"""
    Serializer for get query to users
"""
class SimpleUserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = SimpleUser
        fields = (
            "username",
            "first_name",
            "posts",
        )


"""
    Serializer for get query to user activity
"""
class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ("last_login",)
