# Create your views here.

from rest_framework import generics
from .serializers import (
    IndividualPostSerializer,
    GetAllPostsSerializer,
    GetUserDetailsSerializer,
    CommentSerializer
)
from .models import Post, LikePost, FollowUser, Comment
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# list all posts
class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = GetAllPostsSerializer


# get individual post
class GetPost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = IndividualPostSerializer


# create post
class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = IndividualPostSerializer


# like post
class PostLike(APIView):

    def post(self, request, pk):
        username = self.request.user.username
        # print("userame  ", username)

        post = Post.objects.get(id=pk)

        like_filter = LikePost.objects.filter(
            post_id=pk, username=username).values()

        # print("like_filter  ", like_filter)

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

        # print("like_filter, ", like_filter)

        if like_filter.exists():
            like_filter.delete()
            post.number_of_likes -= 1
            post.save()

        return Response(status=status.HTTP_201_CREATED)


class UserFollow(APIView):

    def post(self, request, pk):
        follower = CustomUser.objects.get(id=self.request.user.id)
        following = CustomUser.objects.get(id=pk)

        # print("user  ", follower)
        # print("to_follow  ", following)

        already_followed = FollowUser.objects.filter(
            user=pk, follower=follower.id).first()

        # print("already_followed  ", already_followed)

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

        # print("user  ", follower)
        # print("to_follow  ", following)

        already_followed = FollowUser.objects.filter(
            user=pk, follower=follower.id).first()

        if already_followed:
            already_followed.delete()
            following.followers -= 1
            following.save()
            follower.followings -= 1
            follower.save()

        return Response(status=status.HTTP_201_CREATED)


class GetUserData(APIView):

    def get(self, request):

        queryset = CustomUser.objects.get(id=self.request.user.id)
        serializer_class = GetUserDetailsSerializer(queryset)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class CommentList(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

# class CommentList(APIView):
#     serializer_class = CommentSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def post(self, request, pk):
#         comment = self.request.data.get("comment")
#         user = self.request.user
#         post_no = pk
#         post = Post.objects.get(id=post_no)
#         serializer_class = CommentSerializer(
#             user=user, comment=comment, post=post)
#         return Response(serializer_class.data, status=status.HTTP_201_CREATED)
