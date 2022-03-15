"""
Instances that make up the Panchatantra: Story, Character
"""
from classes import Story, Character
from pprint import pprint
import csv

instances = []
reader = csv.DictReader(open('cast.csv'), skipinitialspace=True)
for row in reader:
    instances.append(Character(**row))

# cast: Holds all known  instances indexed by name

cast = {c.name: c for c in instances}
# stories: Holds all known Story instances:
stories = {}
stories['book-1'] = Story(title='book-1', cast=cast)
if __name__ == '__main__':
    print("Story:")

    [pprint(vars(c)) for c in cast]
