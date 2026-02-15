from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", login_required(BlogCreateView.as_view()), name="post_new"),
    path("post/<int:pk>/edit/", login_required(BlogUpdateView.as_view()), name="post_edit"),
    path("post/<int:pk>/delete/", login_required(BlogDeleteView.as_view()), name="post_delete"),
]
