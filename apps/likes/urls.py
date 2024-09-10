from django.urls import path

from .views import LikeCreateView

urlpatterns = [
    path(r"", LikeCreateView.as_view(), name="like-create"),
]
