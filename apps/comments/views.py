from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from ..posts.models import Posts

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_slug = self.kwargs["post_slug"]
        return Comment.objects.filter(post__slug=post_slug, parent_comment__isnull=True).order_by("-created_at")

    def perform_create(self, serializer):
        post_slug = self.kwargs["post_slug"]
        post = Posts.objects.get(slug=post_slug)
        serializer.save(post=post)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentReplyView(generics.CreateAPIView):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        parent_comment = Comment.objects.get(pk=self.kwargs["pk"])
        serializer.save(post=parent_comment.post, parent_comment=parent_comment)