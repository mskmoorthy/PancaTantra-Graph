"""
Classes For Panchatantra  Graphs
"""

from pprint import pprint


class DictInit:
    _fields = []

    def __init__(self, **kwargs):
        for name in kwargs.keys():
            if (name in self._fields):
                setattr(self, name, kwargs[name])
            else:
                raise TypeError('Illegal field: {}'.format(name))


class Story(DictInit):
    """Story(title=..., ...) A panchatantra story"""
    _fields = [
        'title', 'told_by', 'told_to', 'moral', 'url', 'cast', 'stories'
    ]

    def show(self):
        "Print out instance."
        for f in self._fields:
            try:
                getattr(self, f)
                pprint(f)
                if (f == 'cast'):
                    [c.show() for c in getattr(self, f)]
                else:
                    pprint(getattr(self, f))
            except AttributeError:
                pass


class Character(DictInit):
    """Character(name = ..., ...) A story character"""
    _fields = ['name', 'species', 'nature', 'color', 'narrated']

    def show(self):
        "Print out instance."
        for f in self._fields:
            try:
                getattr(self, f)
                pprint(f)
                pprint(getattr(self, f))
            except AttributeError:
                pass


if __name__ == '__main__':
    c = Character(name='rusty', species='lion', nature='brave', color='red')
    s = Story(title="Lion, Bull and Two Jackals",
              moral='friendship and villainy ',
              told_by='panchatantra',
              cast=[c],
              stories=[])
    s.show()
