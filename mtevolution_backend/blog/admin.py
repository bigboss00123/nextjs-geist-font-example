from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'content', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('is_featured',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'featured_image')
        }),
        ('Content', {
            'fields': ('summary', 'content')
        }),
        ('Settings', {
            'fields': ('is_featured',)
        })
    )
