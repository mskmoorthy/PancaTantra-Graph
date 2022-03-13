"""
Classes For Panchatantra  Graphs
"""

from pprint import pprint
from utils import Structure  # init helper


class Story(Structure):
    """ A Story consists of Characters, etc."""
    _fields = [
        'title', 'told_by', 'told_to', 'moral', 'url', 'cast', 'stories'
    ]


class Character(Structure):
    """A character in a Story"""
    _fields = [
        'name', 'species', 'nature', 'color', 'said', 'narrated', 'appears_in '
    ]


class Utterance(Structure):
    """An Utterance by a  character in a Story"""
    _fields = ['by', 'to', 'text']


# Example use
if __name__ == '__main__':
    c = Character('rusty', 'lion', 'brave', color='red')
    pprint(vars(c))
s = Story(title="Lion, Bull and Two Jackals",
          moral='friendship and villainy ',
          told_by='panchatantra',
          cast=[c],
          stories=[])
pprint(vars(s))
