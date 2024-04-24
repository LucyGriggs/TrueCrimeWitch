"""
Definition of views.
"""

from typing import Any
from django.shortcuts import render
from .models import Post, Podcast
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from datetime import datetime
# Create your views here.

class PostView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'
  
class PodcastsView(ListView):
  queryset = Podcast.objects.filter(statuspod=1).order_by('-created_on')
  template_name = 'podcasts.html'
  
class SearchView(ListView):
    model = Post
    template_name = "search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
          object_list = Post.objects.filter(Q(title__icontains = query) | Q(content__icontains = query))
          print(object_list)
        else:
          object_list = None
          print(object_list)
          # searchresult = Post.objects.none()
        return object_list
    
    def get_context_data(self, **kwargs):
      context = super(SearchView, self).get_context_data(**kwargs)
      context['query'] = self.request.GET.get('q')
      return context

    
    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     object_list = Post.objects.filter(
    #         Q(title_icontains=query) | Q(content_icontains=query)
    #     )
    #     return object_list

class DetailView(TemplateView):
  model = Post
  template_name = 'post_detail.html'
  
class AboutView(TemplateView):
    template_name="about.html"