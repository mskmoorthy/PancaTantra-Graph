"""
Instances that make up the Panchatantra: Story, Character
"""

from classes import Story, Character
import csv

reader = csv.DictReader(open('cast.csv'), skipinitialspace=True)
cast = {row['name']: Character(**row) for row in reader}

# stories: Holds all known Story instances:
reader = csv.DictReader(open('book-1.csv'), skipinitialspace=True)
stories = {row['title']: Story(**row) for row in reader}

if __name__ == '__main__':
    stories["wedge-pulling monkey"].show()
