from django.test import TestCase
from blog.models import Blog


class BlogTests(TestCase):

    def test_gets_200_on_root_url(self):
        response = self.client.get('/create')
        self.assertEqual(200, response.status_code)

    def test_shows_form_on_root_url(self):
        response = self.client.get('/create')
        self.assertTemplateUsed(response, 'blog/blog_form.html')
        self.assertContains(response, '<form')
        self.assertContains(response, 'method="post"')
        self.assertContains(response, 'name="title"')
        self.assertContains(response, 'type="submit"')

    def test_can_post_blog(self):
        response = self.client.post('/create', {'title': "Hello World"})
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, Blog.objects.count())

    def test_shows_existing_posts_on_root_url(self):
        for i in range(1, 4):
            Blog.objects.create(title=i)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        self.assertEqual(3, len(response.context['object_list']))
