from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import BlogBanner, BlogEntry
from .serializers import BlogBannerSerializer, BlogEntrySerializer

class BlogBannerViewSet(viewsets.ModelViewSet):
    queryset = BlogBanner.objects.all()
    serializer_class = BlogBannerSerializer
    permission_classes = [AllowAny]

class BlogEntryViewSet(viewsets.ModelViewSet):
    queryset = BlogEntry.objects.all().order_by('-created_at')
    serializer_class = BlogEntrySerializer
    permission_classes = [AllowAny]