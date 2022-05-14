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


with open('cast-1.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    cast_1 = {row['name']: Character(**row) for row in reader}

with open('book-1.csv', encoding='utf-8') as f:    
    reader = csv.DictReader(f, skipinitialspace=True)
    book_1 = {row['index']: Story(**row) for row in reader}


with open('cast-2.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    cast_2 = {row['name']: Character(**row) for row in reader}

with open('book-2.csv', encoding='utf-8') as f:    
    reader = csv.DictReader(f, skipinitialspace=True)
    #book_1 = {row['index']: Story(**row) for row in reader}
    book_2 = {row['index']: Story(**row) for row in reader}

stories_finalize(book_1)    
stories_finalize(book_2)

if __name__ == '__main__':
    [book_1[s].show() for s in book_1]
    [book_2[s].show() for s in book_2]
