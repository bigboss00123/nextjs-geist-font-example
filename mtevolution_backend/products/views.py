from django.views.generic import DetailView
from rest_framework import generics
from rest_framework.response import Response
from .models import Product, ProductImage, Testimonial
from .serializers import (
    ProductSerializer, ProductDetailSerializer,
    TestimonialSerializer, ProductImageSerializer
)

# Template Views
class ProductTemplateDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    lookup_field = 'slug'

# API Views
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['is_featured']
    search_fields = ['name', 'description', 'short_description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'

class ProductTestimonialsView(generics.ListAPIView):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(
            product__slug=self.kwargs['slug']
        ).order_by('-created_at')

class ProductGalleryView(generics.ListAPIView):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(
            product__slug=self.kwargs['slug']
        ).order_by('order')

class FeaturedProductsView(generics.ListAPIView):
    queryset = Product.objects.filter(is_featured=True)
    serializer_class = ProductSerializer
    ordering = ['name']
