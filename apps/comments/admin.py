from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author_name", "content", "reply_count")
    search_fields = ("author_name", "content")
    list_filter = ("post",)
    readonly_fields = ("reply_count",)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ("post",)
        return self.readonly_fields
