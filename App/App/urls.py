
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("pages.urls")),
    path('blog/', include("blog.urls")),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),    
    path('carlist/', include("cars.urls")),
    path('accounts/', include("accounts.urls")),
    # path('contact/', include("contact.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
