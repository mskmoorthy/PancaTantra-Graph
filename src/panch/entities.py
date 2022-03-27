"""
Instances that make up the Panchatantra: Story, Character
"""
__author__ = "tv.raman.tv@gmail.com"
import csv
from classes import Story, Character


def stories_finalize(table):
    "Post process stories in table."
    for i in table:
        s = table[i]
        if isinstance(s.stories, str):
            s.stories = s.stories.split()


reader = csv.DictReader(open('cast-1.csv'), skipinitialspace=True)
cast_1 = {row['name']: Character(**row) for row in reader}

reader = csv.DictReader(open('book-1.csv'), skipinitialspace=True)
book_1 = {row['index']: Story(**row) for row in reader}
stories_finalize(book_1)

if __name__ == '__main__':
    [book_1[s].show() for s in book_1]
