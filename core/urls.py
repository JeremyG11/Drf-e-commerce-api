 
from django.contrib import admin
from django.conf import settings
from django.urls import path, include 
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('order/', include('order.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs', SpectacularSwaggerView.as_view(url_name="schema")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
