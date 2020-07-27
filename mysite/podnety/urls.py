from django.urls import path, include
from rest_framework import routers
from podnety.views import PodnetView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('podnety', PodnetView, basename='podnet')

urlpatterns = [
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
