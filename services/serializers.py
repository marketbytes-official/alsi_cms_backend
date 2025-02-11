from rest_framework import serializers
from .models import ServicesTitle, Services

class ServicesTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesTitle
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'image', 'title', 'service_title', 'subtitle', 'link_url', 'banner_image', 'content_paragraphs']