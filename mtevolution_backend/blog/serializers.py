from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', 'post_count']

    def get_post_count(self, obj):
        return obj.posts.count()

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'category', 'category_name',
            'featured_image', 'summary', 'is_featured',
            'created_at', 'updated_at'
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'category',
            'featured_image', 'summary', 'content',
            'is_featured', 'created_at', 'updated_at'
        ]
