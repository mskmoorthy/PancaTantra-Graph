"""
Utility Classes
"""

# Helper: Based on
# https://github.com/dabeaz/python-cookbook/blob/master/src/8/simplified_initialization_of_data_structures/example2.py#start-of-content
# 8.11. Simplifying the Initialization of Data Structures
# Python Cookbook By David Beazley Brian K. Jones


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            kwargs.pop(name, '')

        # Set the remaining keyword arguments
        for name in kwargs.keys():
            if (name in self._fields):
                setattr(self, name, kwargs[name])


# Example use
if __name__ == '__main__':
    class Animal(Structure):
        _fields = ['name', 'species', 'nature']

    a1 = Animal('rusty', 'lion', 'brave')
    a2 = Animal('lively', species='bull', nature='gentle')
    print([v for v in a1._fields])
    print(a1.name, a1.species, a1.nature)
    print(a2.name, a2.species, a2.nature)
