from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage, Testimonial

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text', 'is_primary', 'order', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 1
    fields = [
        ('author', 'role', 'company'),
        'content',
        ('rating', 'is_featured'),
        'avatar'
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'status', 'is_featured', 'featured_image_preview', 'created_at']
    list_filter = ['product_type', 'status', 'is_featured']
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['featured_image_preview', 'created_at']
    inlines = [ProductImageInline, TestimonialInline]
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'slug', 'product_type', 'status', 'is_featured')
        }),
        ('Conteúdo', {
            'fields': ('short_description', 'description', 'features')
        }),
        ('Imagem e URL', {
            'fields': ('featured_image', 'featured_image_preview', 'url')
        }),
        ('Metadados', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.featured_image.url)
        return "No image"
    featured_image_preview.short_description = 'Featured Image Preview'

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_preview', 'alt_text', 'is_primary', 'order']
    list_filter = ['product', 'is_primary']
    search_fields = ['product__name', 'alt_text']
    readonly_fields = ['image_preview']
    ordering = ['product', 'order']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'role', 'rating', 'is_featured', 'avatar_preview']
    list_filter = ['product', 'rating', 'is_featured']
    search_fields = ['author', 'role', 'company', 'content']
    readonly_fields = ['avatar_preview']
    ordering = ['-is_featured', '-created_at']

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 25px;"/>', obj.avatar.url)
        return "No avatar"
    avatar_preview.short_description = 'Avatar Preview'
