from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api import EntityViewSet

router = DefaultRouter()
router.register(r'entity', EntityViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
