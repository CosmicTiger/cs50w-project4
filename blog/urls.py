from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html"), name="home"),
    path('posts/', TemplateView.as_view(template_name="blog/posts.html")),
    path('membership/', TemplateView.as_view(template_name="blog/membership.html")),
    path('faqs/', TemplateView.as_view(template_name="blog/faqs.html")),
    path('about/', TemplateView.as_view(template_name="blog/about.html"))
]
