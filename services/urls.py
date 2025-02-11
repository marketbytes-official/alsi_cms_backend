from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicesTitleViewSet, ServicesViewSet

router = DefaultRouter()
router.register(r'services-banner', ServicesTitleViewSet)
router.register(r'services', ServicesViewSet)

urlpatterns = [
    path('',include(router.urls))
]