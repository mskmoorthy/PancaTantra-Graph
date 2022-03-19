"""
Instances that make up the Panchatantra: Story, Character
"""

from classes import Story, Character
import csv

reader = csv.DictReader(open('cast.csv'), skipinitialspace=True)
cast = {row['name']: Character(**row) for row in reader}

# stories: Holds all known Story instances:
stories = {}
stories['book-1'] = Story(title='book-1', cast=[cast[c] for c in cast])

if __name__ == '__main__':
    stories['book-1'].show()
