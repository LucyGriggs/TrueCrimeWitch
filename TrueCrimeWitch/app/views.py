"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/contact.html',
#         {
#             'title':'Contact',
#             'message':'Your contact page.',
#             'year':datetime.now().year,
#         }
#     )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'About Page/Contact',
            'year':datetime.now().year,
        }
    )

def podcasts(request):
    """Renders the podcasts page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/podcasts.html',
        {
            'title':'Podcasts',
            'message':'List of Podcast Episodes',
            'year':datetime.now().year,
        }
    )
    
# def search(request):
#     """Renders the search function."""
#     assert isinstance(request, HttpRequest)
#     query = request.GET.get('q')
#     podcast_results = Podcast.objects.filter(title__icontains=query)
#     blog_results = Index.objects.filter(title__icontains=query)
#     results = list(podcast_results) + list(blog_results)
#     return render(request,
#         'app/search.html',
#         {
#             'title':'Search Results',
#             'results':results,
#             'year':datetime.now().year,
#         }
#     )