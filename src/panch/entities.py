"""
Instances that make up the Panchatantra: Story, Character
"""
from classes import Story, Character
from pprint import pprint
import csv

values = []
reader = csv.DictReader(open('cast.csv'), skipinitialspace=True)
for row in reader:
    values.append(row)

print(values)

# cast: Holds all known  instances indexed by name
instances = [Character(**dict) for dict in values]
pprint("check first instance")
pprint(vars(instances[0]))
cast = {}
# stories: Holds all known Story instances:
stories = {}
stories['book-1'] = Story(title='book-1', cast=cast)
if __name__ == '__main__':
    print("Story:")
    pprint(vars(stories['book-1']))
