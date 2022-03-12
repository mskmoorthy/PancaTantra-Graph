"""
Classes For Panchatantra  Graphs
"""


class Story:
    """ A Story consists of Characters, etc."""
    title = ""
    stories = []
    narrator = ""
    toldto = ""
    moral = ""
    sanskritverses=[]
    englishmeaning=[]
    cast =[]

class Character:
    """A character in a Story"""
    name = ""
    sanskritname=""
    saidto = []
    narrated = []
    appears_in = []
