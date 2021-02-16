from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog_app/first_page.html"), name='blog_first_page' ),
]