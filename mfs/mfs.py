import copy
import operator
import os
from functools import reduce

from mfs.exceptions import MFSException
from mfs.file import Directory, File


class MFS(object):
    """
    All *_root is a Tree structure
    All *path is a string value
    All route is a path splice list
    """

    def __init__(self, work_path='/'):
        self.work_path = work_path
        # file index
        self.root = Directory()
        self.root['/'] = Directory()

    def pwd(self):
        route = self.split_path(self.work_path)
        nested_route = self.absolute_root(route)
        self.display_files(nested_route)

    def cd(self, path='.'):
        _path = self.parse_rpath(path)
        if self.is_dir_exist(_path):
            self.work_path = _path
        else:
            raise MFSException('Dir is not existed')

    def touch(self, filename, path='.'):
        p_path = self.parent_path(filename)
        filename = os.path.basename(filename)
        if p_path:
            path = p_path
        apath = self.parse_rpath(path)
        target_root = self.path_to_root(path)
        target_root[filename] = File(filename=filename, path=apath)

    def ls(self, rpath='.'):
        apath = self.parse_rpath(rpath)
        if not self.is_dir_exist(apath):
            raise MFSException('Dir is not existed')

        route = self.split_path(apath)
        target_root = self.absolute_root(route)
        self.display_files(target_root)

    def mkdir(self, rpath):
        apath = self.parse_rpath(rpath)
        if self.is_dir_exist(apath):
            raise MFSException('Dir is existed')
        route = self.split_path(apath)
        self.absolute_root(route[:-1])[route[-1]] = Directory()

    def cp_dir(self, source_path, target_path):
        source_root = self.path_to_root(source_path)
        target_apath = self.parse_rpath(target_path)
        route = self.split_path(target_apath)
        if self.is_dir_exist(target_path):
            raise MFSException('Dir is existed')
        self.absolute_root(route[:-1])[route[-1]] = copy.deepcopy(source_root)

    def cp_file(self, source_path, source_filename, target_path, target_filename):
        source_root = self.path_to_root(source_path)
        source_file = source_root[source_filename]
        target_apath = self.parse_rpath(target_path)
        target_root = self.path_to_root(target_path)
        source_file = File(filename=target_filename, path=target_apath,
                           data=source_file.data)
        target_root[target_filename] = source_file

    def tree(self, path='.', depth=0):
        route = self.split_path(self.parse_rpath(path))
        target_root = self.absolute_root(route)
        return self.tree_display(target_root)

    def tree_display(self, t, depth=0):
        if isinstance(t, File):
            return
        for k in t.keys():
            print("|%s|--  %s" % ("".join(depth * ["    "]), k))
            depth += 1
            self.tree_display(t[k], depth)
            depth -= 1

    def read_file(self, file_path):
        if not self.is_dir_exist(file_path):
            raise MFSException('%s is not existed' % file_path)
        target_root = self.path_to_root(file_path)
        return target_root.data

    def write_file(self, file_path, data):
        if not self.is_dir_exist(file_path):
            self.touch(file_path)
        target_root = self.path_to_root(file_path)
        target_root.data = data

    def split_path(self, path):
        result = []
        while path not in ['/', '..', '.']:
            _path, _pos = os.path.split(path)
            path = _path
            if _pos:
                result.append(_pos)
        result.append(path)
        result.reverse()
        return result

    def absolute_root(self, dir_list):
        dir_list = [x for x in dir_list if x]
        return reduce(operator.getitem, dir_list, self.root)

    def path_to_root(self, path):
        path = self.parse_rpath(path)
        route = self.split_path(path)
        return self.absolute_root(route)

    def parent_root(self, apath):
        route = self.split_path(apath)
        if len(route) <= 1:
            return self.root
        return self.absolute_root(route[:-1])

    def parent_path(self, path):
        if path.endswith('/'):
            path = path[:-1]
        return os.path.dirname(path)

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
            if isinstance(leaf[l], File):
                template += str(l)
            else:
                template += str(l) + '/ '
        print(template)

    def is_dir_exist(self, path):
        apath = self.parse_rpath(path)
        route = self.split_path(apath)
        pos = self.root
        for p in route:
            if p in pos.keys():
                pos = pos[p]
            else:
                return False
        return True
