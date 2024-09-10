from django.urls import path

from .views import PostsListCreateView, PostsDetailView

urlpatterns = [
    path(r"", PostsListCreateView.as_view(), name="post-list-create"),
    path(r"<slug:slug>/", PostsDetailView.as_view(), name="post-detail"),
]
