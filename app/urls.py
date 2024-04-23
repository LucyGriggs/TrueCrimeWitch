from .views import PostView, SearchView, DetailView, AboutView, PodcastsView
from django.urls import path

urlpatterns = [
  path('', PostView.as_view(), name="home"),
  path('posts/<slug:slug>/', PostView.as_view(), name="post_detail"),
  path('search/', SearchView.as_view(), name="search_results"),
  path("posts/<slug:slug>/", DetailView.as_view(), name="post_detail"),
  path('about/', AboutView.as_view(), name="about"),
  path('podcasts/', PodcastsView.as_view(), name="podcasts")
]