from rest_framework import serializers
from .models import Service, ServiceProject, ServiceFAQ

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'service_type', 'short_description',
            'featured_image', 'is_featured', 'price_from', 'whatsapp_number'
        ]

class ServiceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProject
        fields = ['id', 'title', 'description', 'image', 'url']

class ServiceFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFAQ
        fields = ['id', 'question', 'answer', 'order']

class ServiceDetailSerializer(serializers.ModelSerializer):
    projects = ServiceProjectSerializer(many=True, read_only=True)
    faqs = ServiceFAQSerializer(many=True, read_only=True)
    feature_list = serializers.ListField(read_only=True)
    whatsapp_link = serializers.CharField(source='get_whatsapp_link', read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'service_type', 'short_description',
            'description', 'feature_list', 'price_from', 'featured_image',
            'whatsapp_number', 'whatsapp_message', 'whatsapp_link',
            'projects', 'faqs', 'created_at'
        ]
