from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'is_published', 'article', 'title', 'publish_date')
    list_display_links = ('author_id', )
    list_editable = ("is_published", 'article', 'title')
    search_fields = ('author_id', 'publish_date')
    list_per_page = 3
    list_filter = ('author_id', 'publish_date')

admin.site.register(Blog, BlogAdmin)


