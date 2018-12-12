from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('search/', include('search.urls', namespace='search')),
    path('messages/', include("pinax.messages.urls", namespace="pinax_messages")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
