from rest_framework import generics, permissions

from .models import Posts
from .serializers import PostsSerializer
from ..common.pagination import DefaultPagination

class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all().order_by("-pub_date")
    serializer_class = PostsSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Only admins can create posts.")
        serializer.save(author=self.request.user)  

class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = "slug"
