import threading
from functools import wraps


def get_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


class memorize(dict):
    """
    Other version
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


def auto_str(cls):
    def f(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))

    cls.__str__ = f
    return cls


def auto_repr(cls):
    def f(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))

    cls.__repr__ = f
    return cls
