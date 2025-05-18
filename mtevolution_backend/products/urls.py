from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Template URLs
    path('<slug:slug>/', views.ProductTemplateDetailView.as_view(), name='product-detail'),

    # API URLs
    path('api/products/', views.ProductListView.as_view(), name='api-product-list'),
    path('api/products/<slug:slug>/', views.ProductDetailView.as_view(), name='api-product-detail'),
    path('api/products/<slug:slug>/testimonials/', views.ProductTestimonialsView.as_view(), name='api-product-testimonials'),
    path('api/products/<slug:slug>/gallery/', views.ProductGalleryView.as_view(), name='api-product-gallery'),
    path('api/products/featured/', views.FeaturedProductsView.as_view(), name='api-featured-products'),
]
