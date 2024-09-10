from django.contrib import admin

from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post",)
    list_filter = ("post",)
    
    def __str__(self):
        return f"Liked a {self.post.title}"
