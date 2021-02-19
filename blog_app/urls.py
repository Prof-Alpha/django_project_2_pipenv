from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog_app/blog.html"), name='blog_first_page' ),
    path('single-post/', TemplateView.as_view(template_name="blog_app/single_post.html"), name='blog_first_page' ),
    path('register/', TemplateView.as_view(template_name="blog_app/register.html"), name='blog_first_page' ),
]