"""
Definition of views.
"""

from django.shortcuts import render
from .models import Post
from django.views import generic 
# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        {
            'title':'About',
            'message':'About Page/Contact',
            'year':datetime.now().year,
        }
    )
    
def post(request):
    """Renders the post page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'post_detail.html',
        {
            'title':'Post',
            'year':datetime.now().year,
        }
    )
    
def search(request):
    """Renders the search function."""
    assert isinstance(request, HttpRequest)
    query = request.GET.get('q')
    blog_results = Index.objects.filter(title__icontains=query)
    results = list(blog_results)
    return render(request,
        'search.html',
        {
            'title':'Search Results',
            'results':results,
            'year':datetime.now().year,
        }
    )