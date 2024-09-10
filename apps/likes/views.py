from rest_framework import generics, status
from rest_framework.response import Response

from .models import Like
from .serializers import LikeSerializer
from ..posts.models import Posts

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        post_slug = request.data.get("post")
        
        post = Posts.objects.get(slug=post_slug)
        
        like, created = Like.objects.get_or_create(post=post)
        
        if not created:
            like.delete()
            return Response({"detail": "Like removed."}, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
