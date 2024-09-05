from django.db import models

from ..posts.models import Posts
from ..common.models import BaseModel as base_model

class Comment(base_model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    content = models.TextField()
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"

    @property
    def reply_count(self):
        return self.replies.count()

    class Meta:
        ordering = ["-created_at"]
