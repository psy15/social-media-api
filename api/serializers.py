# todos/serializers.py
from rest_framework import serializers
from .models import Post, CustomUser, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("comment",)



class GetPostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:

        model = Post
        fields = (
            "id",
            "created_at",
            "number_of_likes",
            "comments"
        )

    def get_comments(self, obj):
        customer_account_query = Comment.objects.filter(
            post=obj.id)
        serializer = CommentSerializer(customer_account_query, many=True)

        return serializer.data


class GetAllPostsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:

        model = Post
        fields = (
            "id",
            "user",
            "title",
            "description",
            "comments",
            "number_of_likes",
            "created_at"
        )

    def get_comments(self, obj):
        customer_account_query = Comment.objects.filter(
            post=obj.id)
        serializer = CommentSerializer(customer_account_query, many=True)

        return serializer.data


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = (
            "title",
            "description",
        )


class GetUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:

        model = CustomUser
        fields = (
            "username",
            "followers",
            "followings",
        )
