# Create your views here.

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    GetPostSerializer,
    GetAllPostsSerializer,
    GetUserDetailsSerializer,
    CommentSerializer,
    CreatePostSerializer
)
from .models import Post, LikePost, FollowUser, Comment
from .models import CustomUser


class ApiOverview(generics.ListAPIView):
    def get(self, request):
        api_urls = {
            'Authenticate': '/authenticate/',
            'Refresh Token': '/token/refresh/',
            'User': '/user/',
            'All posts': '/all_posts/',
            'Create Post': '/posts/',
            'Get and Delete Post': '/posts/<str:pk>',
            'Follow User': '/follow/<str:pk>/',
            'Unfollow User': '/unfollow/<str:pk>/',
            'Like Post': '/like/<str:pk>/',
            'Unlike Post': '/unlike/<str:pk>/',
            'Comment on Post': '/comment/<str:pk>/',
        }
        return Response(api_urls)


# list all posts
# class ListPost(APIView):

#     def get(self, request):
#         queryset = Post.objects.filter(user=self.request.user)
#         serializer_class = GetAllPostsSerializer(queryset, many=True)
#         return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = GetAllPostsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# get individual post
class GetPost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = GetPostSerializer


# create post
class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# like post
class PostLike(APIView):

    def post(self, request, pk):
        username = self.request.user.username

        post = Post.objects.get(id=pk)

        like_filter = LikePost.objects.filter(
            post_id=pk, username=username).values()

        if not like_filter.exists():
            new_like = LikePost.objects.create(
                post_id=pk, username=username)
            new_like.save()
            post.number_of_likes += 1
            post.save()

        return Response(like_filter, status=status.HTTP_201_CREATED)


class PostUnlike(APIView):

    def post(self, request, pk):
        username = self.request.user.username
        post = Post.objects.get(id=pk)

        like_filter = LikePost.objects.filter(
            post_id=pk, username=username)

        if like_filter.exists():
            like_filter.delete()
            post.number_of_likes -= 1
            post.save()

        return Response(status=status.HTTP_201_CREATED)


class UserFollow(APIView):

    def post(self, request, pk):
        follower = CustomUser.objects.get(id=self.request.user.id)
        following = CustomUser.objects.get(id=pk)

        already_followed = FollowUser.objects.filter(
            user=pk, follower=follower.id).first()

        if not already_followed:
            new_follower = FollowUser.objects.create(
                user=pk, follower=follower.id)
            new_follower.save()
            following.followers += 1
            following.save()
            follower.followings += 1
            follower.save()

        return Response(status=status.HTTP_201_CREATED)


class UserUnfollow(APIView):

    def post(self, request, pk):

        follower = CustomUser.objects.get(id=self.request.user.id)
        following = CustomUser.objects.get(id=pk)

        already_followed = FollowUser.objects.filter(
            user=pk, follower=follower.id).first()

        if already_followed:
            already_followed.delete()
            following.followers -= 1
            following.save()
            follower.followings -= 1
            follower.save()

        return Response(status=status.HTTP_201_CREATED)


# class GetUserData(APIView):

#     def get(self, request):

#         queryset = CustomUser.objects.get(id=self.request.user.id)
#         serializer_class = GetUserDetailsSerializer(queryset)
#         return Response(serializer_class.data, status=status.HTTP_201_CREATED)

class GetUserData(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetUserDetailsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)


class CommentList(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        post=Post.objects.get(id=self.kwargs.get('pk')))

    def get_queryset(self):
        return super().get_queryset().filter(post=self.kwargs.get('pk'))
