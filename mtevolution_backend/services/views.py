from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Service, ServiceProject, ServiceFAQ

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    queryset = Service.objects.filter(status='ACTIVE')

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        context['projects'] = ServiceProject.objects.filter(service=service)
        context['faqs'] = ServiceFAQ.objects.filter(service=service).order_by('order')
        return context
