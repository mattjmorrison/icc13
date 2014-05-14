class Blog(object):

    def __init__(self, persistence):
        self.persistence = persistence
        self.posts = self.persistence.get()

    def create_post(self, title):
        self.posts.append(title)
        self.persistence.put(self.posts)
