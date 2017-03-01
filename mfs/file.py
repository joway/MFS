class File(object):
    def __init__(self, filename: str, path: str, permission: str = '0666'):
        self.filename = filename
        self.path = path
        self.permission = permission
