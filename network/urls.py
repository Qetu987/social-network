from django.urls import path
from .views import (
    PostListView,
    SimpleListViev,
    UserCreateView,
    PostLikeView,
    PostDislikeView,
    AnaliticsLikesView,
    AnaliticsDislikesView,
    login,
)


urlpatterns = [
    path("api/posts/", PostListView.as_view()),
    path("api/users/", SimpleListViev.as_view()),
    path("api/create_user/", UserCreateView.as_view()),
    path("api/like/", PostLikeView.as_view()),
    path("api/dislike/", PostDislikeView.as_view()),
    path(
        "api/likeanalitics/date_from=<date_from>&date_to=<date_to>/",
        AnaliticsLikesView.as_view(),
    ),
    path(
        "api/dislikeanalitics/date_from=<date_from>&date_to=<date_to>/",
        AnaliticsDislikesView.as_view(),
    ),
    path("api/login/", login, name="login"),
]
