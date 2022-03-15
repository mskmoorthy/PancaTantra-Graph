"""
Utility Classes
"""

from pprint import pprint

# Helper: Based on
# https://github.com/dabeaz/python-cookbook/blob/master/src/8/simplified_initialization_of_data_structures/example2.py#start-of-content


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            if (name in kwargs):
                raise TypeError('Duplicate values for {}'.format(
                    ','.join(kwargs)))
        # Set the remaining keyword arguments
        for name in kwargs.keys():
            if (name in self._fields):
                setattr(self, name, kwargs[name])
            else:
                raise TypeError('Illegal field: {}'.format(name))


# Example use
if __name__ == '__main__':

    class Animal(Structure):
        _fields = ['name', 'species', 'nature']

    a1 = Animal('rusty', 'lion', 'brave')
    a2 = Animal('lively', species='bull', nature='gentle')
    pprint(a1._fields)
    pprint(vars(a1))
    pprint(vars(a2))
