from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('b2b/', include('b2b_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('b2b_app.urls'), name="b2b"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
