import operator
import os
from functools import reduce

from mfs.file import Directory


class MFS(object):
    """
    All *_root is a Tree structure
    All *path is a string value
    All route is a path splice list
    """

    def __init__(self, work_path='/'):
        self.work_path = work_path
        self.root = Directory()

    def pwd(self):
        route = self.split_path(self.work_path)
        nested_route = self.absolute_root(route)
        self.display_files(nested_route)

    def cd(self, path='.'):
        self.work_path = self.parse_rpath(path)

    def touch(self, path='.', filename=''):
        apath = self.parse_rpath(path)

    def ls(self, rpath='.'):
        apath = self.parse_rpath(rpath)
        route = self.split_path(apath)
        target_root = self.absolute_root(route)
        self.display_files(target_root)

    def mkdir(self, rpath):
        apath = self.parse_rpath(rpath)
        route = self.split_path(apath)
        self.absolute_root(route[:-1])[route[-1]] = Directory()

    def cp(self, source, target):
        pass

    def tree(self, path='.', depth=0):
        route = self.split_path(self.parse_rpath(path))
        target_root = self.absolute_root(route)
        return self.tree_display(target_root)

    def tree_display(self, t, depth=0):
        for k in t.keys():
            print("|%s|--  %s" % ("".join(depth * ["    "]), k))
            depth += 1
            self.tree_display(t[k], depth)
            depth -= 1

    def read_file(self, file_path):
        pass

    def write_file(self, file_path):
        pass

    def split_path(self, path):
        result = []
        while path not in ['/', '..', '.']:
            _path, _pos = os.path.split(path)
            path = _path
            result.append(_pos)
        result.append(path)
        result.reverse()
        return result

    def absolute_root(self, dir_list):
        dir_list = [x for x in dir_list if x]
        return reduce(operator.getitem, dir_list, self.root)

    def parent_root(self, apath):
        route = self.split_path(apath)
        if len(route) <= 1:
            return self.root
        return self.absolute_root(route[:-1])

    def parent_path(self, path):
        return os.path.dirname(path) + '/'

    def parse_rpath(self, rpath: str):
        """
        :param rpath: relative path 
        :return: apath: absolute path 
        """
        if rpath.startswith('/'):
            return rpath
        elif rpath.startswith('.'):
            # "." or ".."
            target_path = self.work_path
            for i in self.split_path(rpath):
                if i == '..':
                    target_path = self.parent_path(target_path)
                elif i == '.':
                    continue
                else:
                    break
            return target_path
        else:
            return '%s%s/' % (self.work_path, rpath)

    def display_files(self, leaf):
        template = ''
        for l in leaf:
            template += str(l) + '/ '
        print(template)
