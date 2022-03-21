"""
Instances that make up the Panchatantra: Story, Character
"""
__author__ = "tv.raman.tv@gmail.com"
from classes import Story, Character
import csv


def stories_finalize(table):
    "Post process stories in table."
    for id in table:
        s = table[id]
        if (isinstance(s.stories, str)):
            s.stories = s.stories.split()


reader = csv.DictReader(open('cast-1.csv'), skipinitialspace=True)
cast_1 = {row['name']: Character(**row) for row in reader}

# stories: Holds all known Story instances:
reader = csv.DictReader(open('book-1.csv'), skipinitialspace=True)
book_1 = {row['index']: Story(**row) for row in reader}
stories_finalize(book_1)

if __name__ == '__main__':
    [book_1[s].show() for s in book_1]
