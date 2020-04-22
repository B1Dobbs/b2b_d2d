from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api_app import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('b2b_app.urls'), name="b2b"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', csrf_exempt(views.SearchAPI.as_view()), name="api"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
