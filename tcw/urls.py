"""
Definition of urls for tcw.
"""

from django.contrib import admin
from django.urls import path, include
from app import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('post/', views.post, name='post'),
    
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico')))
    
]
