from rest_framework import serializers
from .models import Product, ProductImage, Testimonial

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'created_at']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'client_name', 'client_company', 'client_image',
            'content', 'rating', 'is_featured', 'created_at'
        ]

class ProductSerializer(serializers.ModelSerializer):
    primary_image = serializers.SerializerMethodField()
    testimonial_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'short_description',
            'featured_image', 'is_featured', 'primary_image',
            'testimonial_count', 'created_at', 'updated_at'
        ]

    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return ProductImageSerializer(primary_image).data
        return None

    def get_testimonial_count(self, obj):
        return obj.testimonials.count()

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True, read_only=True)
    featured_testimonials = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'short_description',
            'featured_image', 'features', 'tech_specs', 'is_featured',
            'images', 'testimonials', 'featured_testimonials',
            'created_at', 'updated_at'
        ]

    def get_featured_testimonials(self, obj):
        featured = obj.testimonials.filter(is_featured=True)[:3]
        return TestimonialSerializer(featured, many=True).data
