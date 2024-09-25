from django import forms
from django.contrib import admin

from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    form = PostsForm
    list_display = ("title", "slug", "created_at", "author", "like_count", "comment_count")
    search_fields = ("title", "content", "author__username")
    readonly_fields = ("like_count", "comment_count")

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ("slug",)
        return self.readonly_fields

    def get_prepopulated_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return {} 
        return {"slug": ("title",)}  # Prepopulate slug for new objects