from .views import PostView, SearchView, DetailView, AboutView
from django.urls import path

urlpatterns = [
  path('', PostView.as_view(), name="home"),
  path('posts/<slug:slug>/', PostView.as_view(), name="post_detail"),
  path('search/', SearchView.as_view(), name="search_results"),
  path("posts/<int:pk>/", DetailView.as_view(), name="post_detail"),
  path('about/', AboutView.as_view(), name="about")
]