from django.contrib import admin

from .models import Contacts

class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'car', 'email', 'phone', 'contact_date', 'is_published', 'testimonial')
    list_display_links = ('id', 'name', 'email', 'car')
    search_fields = ('name', 'email', 'car')
    list_editable = ("is_published",'testimonial')
    list_filter = ('car', 'phone', 'name')
    pagination = 25    
admin.site.register(Contacts, ContactAdmin)


