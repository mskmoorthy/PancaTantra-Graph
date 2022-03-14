"""
Instances that make up the Panchatantra: Story, Character
"""
from classes import Story, Character
from pprint import pprint

# cast: Holds all known Character instances:
cast = {}

# Will be eventually read from a data file.

cast['rusty'] = Character(name='rusty', species='lion', color='red')
cast['lively'] = Character(name='lively', species='bull', color='blue')
cast['crafty'] = Character(name='crafty', species='jackal', color='green')
cast['cautious'] = Character(name='cautious', species='jackal', color='yellow')

# stories: Holds all known Story instances:
# Will be eventually read from a data file.

stories = {}

stories['book-1'] = Story(title='book-1', cast=cast)

if __name__ == '__main__':
    pprint(vars(stories['book-1']))
    [pprint(vars(c)) for _, c in cast.items()]
