from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from ..common.models import BaseModel as base_model

class Posts(base_model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            
            title_without_numbers = "".join([i for i in self.title if not i.isdigit()])
            base_slug = slugify(title_without_numbers[:50])
        
            self.slug = base_slug

            super().save(*args, **kwargs)

            if Posts.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{self.pk}"

        super().save(*args, **kwargs)

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def comment_count(self):
        return self.comments.count()