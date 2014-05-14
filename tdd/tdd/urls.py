from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns(
    '',
    url(r'^create$', views.AddBlog.as_view()),
    url(r'^$', views.ListBlogs.as_view()),
)
