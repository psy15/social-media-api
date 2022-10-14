# todos/serializers.py
from rest_framework import serializers
from .models import Post, CustomUser, Comment


class IndividualPostSerializer(serializers.ModelSerializer):
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:

        model = Post
        fields = (
            "id",
            "user",
            "title",
            "description",
            "created_at",
            "number_of_likes"
        )


class GetAllPostsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = (
            "id",
            "title",
            "description",
            # "comments",
            "number_of_likes",
            "created_at"
        )


class GetUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = (
            "username",
            "followers",
            "followings",
        )


# class CommentSerializer(serializers.ModelSerializer):

#     # user = serializers.ReadOnlyField()
#     # comment = serializers.ReadOnlyField("comment")
#     # post = serializers.ReadOnlyField("post")

#     class Meta:
#         model = Comment
#         fields = (
#             "user",
#             "comment",
#             "post"
#         )

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user')
#         comment = kwargs.pop('comment')
#         post = kwargs.pop('post')
#         print(user, comment, post)
#         super().__init__(*args, **kwargs)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            "user",
            "comment",
            "post"
        )
