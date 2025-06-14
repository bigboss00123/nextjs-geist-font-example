from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service-list'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='service-detail'),
]
