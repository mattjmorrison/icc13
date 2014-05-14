import pickle
from os import path
from os import remove


class Persistence(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def get(self):
        if not path.isfile(self.file_path):
            return []
        with open(self.file_path, 'r') as f:
            return pickle.load(f)

    def put(self, data):
        with open(self.file_path, 'a') as f:
            pickle.dump(data, f)

    def delete(self):
        if path.isfile(self.file_path):
            remove(self.file_path)
