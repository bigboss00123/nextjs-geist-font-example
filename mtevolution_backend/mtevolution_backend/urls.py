from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin site
admin.site.site_header = 'MTevolution Admin'
admin.site.site_title = 'MTevolution Admin Portal'
admin.site.index_title = 'Bem-vindo ao Portal Administrativo da MTevolution'
