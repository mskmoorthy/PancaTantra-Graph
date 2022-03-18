"""
Utility Classes
"""

from pprint import pprint

# Helper: Based on
# https://github.com/dabeaz/python-cookbook/blob/master/src/8/simplified_initialization_of_data_structures/example2.py#start-of-content


# Only takes    keyword arguments
class Structure:
    _fields = []

    def __init__(self, **kwargs):
        for name in kwargs.keys():
            if (name in self._fields):
                setattr(self, name, kwargs[name])
            else:
                raise TypeError('Illegal field: {}'.format(name))


# Example use
if __name__ == '__main__':

    class Animal(Structure):
        _fields = ['name', 'species', 'nature']

    a1 = Animal(name='rusty', species='lion', nature='brave')
    a2 = Animal(name='lively', species='bull', nature='gentle')
    pprint(a1._fields)
    pprint(vars(a1))
    pprint(vars(a2))
