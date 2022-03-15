"""
Instances that make up the Panchatantra: Story, Character
"""

from classes import Story, Character
from pprint import pprint
import csv

reader = csv.DictReader(open('cast.csv'), skipinitialspace=True)
cast = {row['name']: Character(**row) for row in reader}
# stories will be read in from a csv file:
# stories: Holds all known Story instances:
stories = {}
stories['book-1'] = Story(index='s1', title='book-1', cast=cast)

if __name__ == '__main__':
    print("Story:")
    pprint(vars(stories['book-1']))
    [pprint(vars(v)) for v in cast.values()]
