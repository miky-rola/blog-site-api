from rest_framework import serializers

from .models import Comment


class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveCommentSerializer(many=True, read_only=True)
    reply_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id", 
            "post", 
            "parent_comment", 
            "content", "author_name", 
            "created_at", 
            "replies", 
            "reply_count"
        ]
