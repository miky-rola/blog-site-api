from rest_framework import generics

from .models import Posts
from .serializers import PostsSerializer
from ..common.pagination import DefaultPagination

class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all().order_by("-pub_date")
    serializer_class = PostsSerializer
    pagination_class = DefaultPagination

class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = "slug"
