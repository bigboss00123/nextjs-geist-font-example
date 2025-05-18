from django.contrib import admin
from django.utils.html import format_html
from .models import Service, ServiceProject, ServiceFAQ

class ServiceProjectInline(admin.StackedInline):
    model = ServiceProject
    extra = 1
    fields = ['title', 'description', 'image', 'url', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1
    fields = ['question', 'answer', 'order']
    ordering = ['order']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'status', 'is_featured', 'featured_image_preview', 'created_at']
    list_filter = ['service_type', 'status', 'is_featured']
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['featured_image_preview', 'created_at']
    inlines = [ServiceProjectInline, ServiceFAQInline]

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'slug', 'service_type', 'status', 'is_featured')
        }),
        ('Conteúdo', {
            'fields': ('short_description', 'description', 'features')
        }),
        ('Preço', {
            'fields': ('price_from',),
        }),
        ('WhatsApp', {
            'fields': ('whatsapp_number', 'whatsapp_message'),
            'description': 'Configurações para o botão de contato via WhatsApp'
        }),
        ('Imagem', {
            'fields': ('featured_image', 'featured_image_preview')
        }),
        ('Metadados', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.featured_image.url)
        return "No image"
    featured_image_preview.short_description = 'Featured Image Preview'

@admin.register(ServiceProject)
class ServiceProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'image_preview', 'url']
    list_filter = ['service']
    search_fields = ['title', 'description', 'service__name']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(ServiceFAQ)
class ServiceFAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'service', 'order']
    list_filter = ['service']
    search_fields = ['question', 'answer', 'service__name']
    ordering = ['service', 'order']
