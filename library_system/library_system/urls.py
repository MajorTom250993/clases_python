from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from books import urls as books_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include((books_urls, 'books'), namespace='books')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
