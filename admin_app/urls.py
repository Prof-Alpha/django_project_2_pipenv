from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='admin_app/dashboard.html')),
]