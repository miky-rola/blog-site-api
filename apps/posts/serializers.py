from rest_framework import serializers

from .models import Posts
from ..comments.serializers import CommentSerializer
from ..likes.serializers import LikeSerializer


class PostsSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = [
            "id", 
            "title", 
            "slug", 
            "content", 
            "created_at", 
            "author", 
            "image",
            "like_count", 
            "comment_count", 
            "likes", 
            "comments"
        ]

    def get_comments(self, obj):
        comments = obj.comments.filter(parent_comment__isnull=True)
        return CommentSerializer(comments, many=True).data
