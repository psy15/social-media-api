from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,  # new
)
from .views import (
    ListPost,
    GetPost,
    CreatePost,
    PostLike,
    PostUnlike,
    UserFollow,
    UserUnfollow,
    GetUserData,
    CommentList,
    ApiOverview
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # done
    path('', ApiOverview().as_view(), name="api-overview"),
    path("all_posts/", ListPost().as_view(), name="all_posts"),
    path("posts/", CreatePost().as_view(), name="create_post"),
    path("posts/<int:pk>/", GetPost().as_view(),
         name="crud_post"),
    path("like/<int:pk>/", PostLike().as_view(), name="like_post"),
    path("unlike/<int:pk>/", PostUnlike().as_view(), name="unlike_post"),
    path("follow/<int:pk>/", UserFollow().as_view(), name="follow_user"),
    path("unfollow/<int:pk>/", UserUnfollow().as_view(), name="unfollow_user"),
    path("user", GetUserData().as_view(), name="user_profile"),
    path("comment/<int:pk>/", CommentList().as_view(), name="comment_on_post"),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(
        url_name="schema"), name="redoc",),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(
        url_name="schema"), name="swagger-ui"),  # new
]
