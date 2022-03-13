"""
Classes For Panchatantra  Graphs
"""

# Helper: Based on
# 8.11. Simplifying the Initialization of Data Structures
# Python Cookbook By David Beazley Brian K. Jones
# See https://github.com/dabeaz/python-cookbook


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in kwargs.keys():
            if (name in self._fields):
                setattr(self, name, kwargs[name])


class Story(Structure):
    """ A Story consists of Characters, etc."""
    _fields = ['title', 'narrator', 'moral', 'cast', 'stories']
    id  # unique id (computed)


class Character(Structure):
    """A character in a Story"""
    _fields = ['name', 'said', 'narrated', 'appears_in ']
    id  # Unique id (computed)


class Utterance(Structure):
    """An Utterance by a  character in a Story"""
    _fields = ['by', 'to', 'text']
    id  # Unique id (computed)
