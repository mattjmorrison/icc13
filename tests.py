import unittest
from blog import Blog
from persistence.file_persistence import Persistence


class BlogTests(unittest.TestCase):

    def setUp(self):
        self.persistence = Persistence('/tmp/blog.txt')

    def tearDown(self):
        self.persistence.delete()

    def test_can_create_post(self):
        blog = Blog(self.persistence)
        blog.create_post("Hello World")
        self.assertEqual(len(blog.posts), 1)

    def test_can_persist_posts(self):
        blog1 = Blog(self.persistence)
        blog1.create_post("Hello World")
        blog2 = Blog(self.persistence)
        self.assertEqual(len(blog2.posts), 1)

    def test_new_blog_has_no_posts(self):
        blog = Blog(self.persistence)
        self.assertEqual(len(blog.posts), 0)
