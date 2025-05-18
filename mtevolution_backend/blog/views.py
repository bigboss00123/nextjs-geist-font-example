from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer, PostDetailSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['category', 'is_featured']
    search_fields = ['title', 'content', 'summary']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class FeaturedPostsView(generics.ListAPIView):
    queryset = Post.objects.filter(is_featured=True)
    serializer_class = PostSerializer
    ordering = ['-created_at']
