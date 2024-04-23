from django.contrib import admin

#Register your models here

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on','image')
    list_filter = ('status',)
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)

from .models import Podcasts

class PodcastAdmin(admin.ModelAdmin):
    list_display = ('titlepod', 'statuspod', 'created_on', 'apple', 'spotify', 'spreaker', 'castbox')
    list_filter = ('statuspod',)
    search_fields = ['titlepod', 'contentpod']
    
admin.site.register(Podcasts, PodcastAdmin)