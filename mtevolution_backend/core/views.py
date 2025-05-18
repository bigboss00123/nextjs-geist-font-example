from django.views.generic import TemplateView
from products.models import Product
from services.models import Service

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(status='LIVE')  # Changed from 'ACTIVE' to 'LIVE'
        context['services'] = Service.objects.filter(status='ACTIVE')
        return context
