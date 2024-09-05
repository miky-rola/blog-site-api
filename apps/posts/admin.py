from django.contrib import admin
from .models import Posts

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "pub_date", "author", "like_count", "comment_count")
    search_fields = ("title", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("like_count", "comment_count")

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ("slug",)
        return self.readonly_fields
