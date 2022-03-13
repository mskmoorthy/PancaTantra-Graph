"""
Classes For Panchatantra  Graphs
"""
from utils import Structure  # init helper


class Story(Structure):
    """ A Story consists of Characters, etc."""
    _fields = ['title', 'narrator', 'moral', 'cast', 'stories']
    id  # unique id (computed)


class Character(Structure):
    """A character in a Story"""
    _fields = ['name',  'species', 'nature', 'said', 'narrated', 'appears_in ']
    id  # Unique id (computed)


class Utterance(Structure):
    """An Utterance by a  character in a Story"""
    _fields = ['by', 'to', 'text']
    id  # Unique id (computed)


# Example use
if __name__ == '__main__':
    c = Character('rusty', 'lion', 'brave')
    print(c.name, c.species, c.nature)
s = Story(
    title="Lion, Bull and Two Jackals",
    moral='friendship and villany ',
    narrator='panchatantra',
    stories=[])
print(s.title, s.narrator, s.moral, s.stories)
