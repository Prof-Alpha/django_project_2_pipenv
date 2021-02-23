from django.urls import path
from django.views.generic import TemplateView
from .views import BlogTestView, BlogCreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog_app/blog.html"), name='blog_first_page' ),
    path('single-post/', TemplateView.as_view(template_name="blog_app/single_post.html"), name='blog_first_page' ),
    path('register/', TemplateView.as_view(template_name="blog_app/register.html"), name='blog_first_page' ),

    #test
    path('test-blog', BlogTestView.as_view(template_name='blog_app/blog_test.html') , name='blog_test'),
    path('test-create', BlogCreateView.as_view(template_name='blog_app/create_test.html') , name='create_test'),
]