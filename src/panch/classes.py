"""
Classes For Panchatantra  Graphs
"""


from utils import Structure  # init helper


class Story(Structure):
    """ A Story consists of Characters, etc."""
    _fields = ['title', 'told_by', 'told_to',
               'moral', 'url', 'cast', 'stories']


class Character(Structure):
    """A character in a Story"""
    _fields = ['name',  'species', 'nature', 'said', 'narrated', 'appears_in ']


class Utterance(Structure):
    """An Utterance by a  character in a Story"""
    _fields = ['by', 'to', 'text']


# Example use
if __name__ == '__main__':
    c = Character('rusty', 'lion', 'brave')
    print(c.name, c.species, c.nature)
s = Story(
    title="Lion, Bull and Two Jackals",
    moral='friendship and villany ',
    told_by='panchatantra',
    stories=[])
print(s.title, s.told_by, s.moral, s.stories)
