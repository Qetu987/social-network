from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .serializers import (
    PostSerializer,
    SimpleUserSerializer,
    LikeSerializer,
    DislikeSerializer,
    UserActivitySerializer,
    PostPostSerializer,
    LikePostSerializer,
    DislikePostSerializer,
)

from .models import Post, Like, Dislike, SimpleUser

import json

from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.authtoken.models import Token


"""
    View for list of user 
    Get query
"""
class SimpleListViev(APIView):
    def get(self, request):
        user = SimpleUser.objects.all()
        print(user)
        serializer = SimpleUserSerializer(user, many=True)
        return Response(serializer.data)


"""
    View for post 
    Get query and post query
"""
class PostListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        post = PostPostSerializer(data=request.data)
        if post.is_valid():
            post.save()
        return Response(request.data, status=201)


"""
    View post query for post
"""
class PostLikeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        post = LikePostSerializer(data=request.data)
        if post.is_valid():
            post.save()
        return Response(request.data, status=201)


"""
    View post query for like
"""
class PostDislikeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        post = DislikePostSerializer(data=request.data)
        if post.is_valid():
            post.save()
        return Response(request.data, status=201)


"""
    View create query for new user
"""
class UserCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


"""
    View get query for analitic of likes by period
"""
class AnaliticsLikesView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        likes_analitic = Like.objects.filter(
            date__range=[kwargs["date_from"], kwargs["date_to"]]
        )
        if len(likes_analitic) > 0:
            mimetype = "application/json"
            return HttpResponse(
                json.dumps({"likes by period": len(likes_analitic)}), mimetype
            )
        else:
            return self.list(request, *args, [{}])


"""
    View get query for analitic of dislikes by period
"""
class AnaliticsDislikesView(generics.ListAPIView):
    serializer_class = DislikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        likes_analitic = Dislike.objects.filter(
            date__range=[kwargs["date_from"], kwargs["date_to"]]
        )
        if len(likes_analitic) > 0:
            mimetype = "application/json"
            return HttpResponse(
                json.dumps({"dislikes by period": len(likes_analitic)}), mimetype
            )
        else:
            return self.list(request, *args, [{}])


"""
    View login query for user
"""
@csrf_exempt
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({"error": "wrong user data"}, status=HTTP_400_BAD_REQUEST)

    user = SimpleUser.objects.get(username=username, password=password)
    if request.user.is_authenticated:
        print("user is authenticated")
    else:
        print("User is not authenticated")
    if not user:
        return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=HTTP_200_OK)
