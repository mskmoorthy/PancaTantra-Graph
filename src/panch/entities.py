"""
Instances that make up the Panchatantra: Story, Character
"""

from classes import Story, Character
import csv
from pprint import pprint

reader = csv.DictReader(open('cast.csv'), skipinitialspace=True)
cast = {row['name']: Character(**row) for row in reader}

# stories: Holds all known Story instances:
stories = {}
stories['book-1'] = Story(title='book-1', cast=[cast[c] for c in cast])

if __name__ == '__main__':
    print("Story:")
    stories['book-1'].show()
