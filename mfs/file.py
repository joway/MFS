from collections import defaultdict


def Directory():
    return defaultdict(Directory)


class File(object):
    def __init__(self, filename: str, path: str, data='', permission: str = '0666'):
        self.filename = filename
        self.path = path
        self.data = data
        self.permission = permission

    def __str__(self):
        return self.filename

    def read(self):
        return self.data

    def write(self):
        return self.data
