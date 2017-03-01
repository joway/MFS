import operator
from functools import reduce


def get_nested(root, keys):
    return reduce(operator.getitem, keys, root)


def set_nested(root, keys, value):
    get_nested(root, keys[:-1])[keys[-1]] = value
