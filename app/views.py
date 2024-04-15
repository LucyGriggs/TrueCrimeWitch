"""
Definition of views.
"""

from typing import Any
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from datetime import datetime
# Create your views here.

class PostView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'
  
class SearchView(ListView):
    model = Post
    template_name = "search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
          result = Post.objects.filter(title__contains = query) | Post.objects.filter(content__contains = query)
        else:
          result = None
        return result
    
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