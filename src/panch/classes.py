"""
Classes For Panchatantra  Graphs
"""

from pprint import pprint
from utils import Structure  # init helper


class Story(Structure):
    """ A Story consists of Characters, etc."""
    _fields = [
        'index', 'title', 'told_by', 'told_to', 'moral', 'url', 'cast',
        'stories'
    ]


class Character(Structure):
    """A character in a Story"""
    _fields = ['name', 'species', 'nature', 'color', 'narrated']


# Example use
if __name__ == '__main__':
    c = Character(name='rusty', species='lion', nature='brave', color='red')
    pprint(vars(c))
    s = Story(title="Lion, Bull and Two Jackals",
              moral='friendship and villainy ',
              told_by='panchatantra',
              cast=[c],
              stories=[])
    pprint(vars(s))
