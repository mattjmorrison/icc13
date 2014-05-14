from django.views.generic.edit import CreateView
from django.views.generic import ListView
from blog.models import Blog


class AddBlog(CreateView):
    model = Blog

    def get_success_url(self):
        return '/'


class ListBlogs(ListView):
    model = Blog
