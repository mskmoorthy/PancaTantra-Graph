"""
Classes For Panchatantra  Graphs
"""
__author__ = "tv.raman.tv@gmail.com"


class DictInit:
    _fields = []

    def __init__(self, **kwargs):
        for name in kwargs.keys():
            if name in self._fields:
                setattr(self, name, kwargs[name])
            else:
                raise TypeError('Illegal field: {}'.format(name))


class Story(DictInit):
    """Story(title=..., ...) A panchatantra story"""
    _fields = [
        'index',
        'title',
        'told_by',
        'told_to',
        'moral',
        'stories',
    ]

    def show(self):
        "Print out instance."
        for f in self._fields:
            try:
                v = getattr(self, f)
                if v is not None:
                    print(f, ": ", v)
            except AttributeError:
                pass


class Character(DictInit):
    """Character(name = ..., ...) A story character"""
    _fields = ['name', 'species', 'color', 'nature', 'narrated', 'primary']

    def show(self):
        "Print out instance."
        for f in self._fields:
            try:
                v = getattr(self, f)
                print("{}: {}".format(f, v))
            except AttributeError:
                pass
