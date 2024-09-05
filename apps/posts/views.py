from rest_framework import generics
from .models import Posts
from .serializers import PostsSerializer

class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all().order_by("-pub_date")
    serializer_class = PostsSerializer

class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    lookup_field = "slug"
