from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ServicesTitle, Services
from .serializers import ServicesTitleSerializer, ServicesSerializer

class ServicesTitleViewSet(viewsets.ModelViewSet):
    queryset = ServicesTitle.objects.all()
    serializer_class = ServicesTitleSerializer
    permission_classes = [AllowAny]

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]
