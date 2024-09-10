from django.urls import path

from .views import (
    CommentListCreateView, 
    CommentDetailView, 
    CommentReplyView
)

urlpatterns = [
    path(r"<slug:post_slug>/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path(r"<uuid:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path(r"<uuid:pk>/reply/", CommentReplyView.as_view(), name="comment-reply"),
]
