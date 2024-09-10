from django.db import models

from ..posts.models import Posts
from ..common.models import BaseModel as base_model

class Like(base_model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("post",)

    def __str__(self):
        return f"Liked a {self.post.title}"
