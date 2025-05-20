from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'last_updated']
    date_hierarchy = 'date_created'
    ordering = ['date_created']
    search_fields = ['title', 'body']

admin.site.register(Post, PostAdmin)