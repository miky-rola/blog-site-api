from django.urls import include, path

app_name = "api"

urlpatterns = [
    path(r"posts/", include("apps.posts.urls")),
    path(r"likes/", include("apps.likes.urls")),
    path(r"comment/", include("apps.comments.urls"))   
]