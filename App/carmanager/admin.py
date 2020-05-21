from django.contrib import admin

from .models import CarManager

class CarManagersAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'phone1', 'position', 'telegram', 'is_published')
    list_display_links = ("name", "phone1", 'email', 'telegram')
    list_editable = ("is_published",)
    search_fields = ("name", 'phone1', 'phone2', 'phone3', 'email', 'telegram',)
    list_per_page = 7
    list_filter = ("position", 'telegram', 'hire_date')

admin.site.register(CarManager, CarManagersAdmin)
